from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import re
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Cybersecurity Forensic Dashboard API")

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REPORTS_DIR = r"l:\Study material\GUI_Assignment\Report"

class Finding(BaseModel):
    finding: str
    implication: str

class ReportMetadata(BaseModel):
    filename: str
    title: str
    risk_level: str
    forensic_value: str
    sensitivity: str
    summary_preview: str
    findings: List[Finding] = []

class Stats(BaseModel):
    total_files: int
    high_risk_count: int
    medium_risk_count: int
    low_risk_count: int
    critical_findings_count: int

def parse_md_file(file_path: str) -> Optional[ReportMetadata]:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        filename = os.path.basename(file_path)
        
        # Extract Title (First line usually)
        title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filename
        
        # Extract Sensitivity
        sensitivity_match = re.search(r"\*\*Data Sensitivity Level:\*\*\s*(.+)", content)
        sensitivity = sensitivity_match.group(1).strip() if sensitivity_match else "Unknown"
        
        # Extract Forensic Value
        value_match = re.search(r"\*\*Forensic Value:\*\*\s*(.+)", content)
        forensic_value = value_match.group(1).strip() if value_match else "Unknown"
        
        # Extract Executive Summary
        # Look for ## 6. Executive Summary and grab the content until next header or end
        summary_match = re.search(r"## 6\. Executive Summary\s*(.+?)(?=\n##|\Z)", content, re.DOTALL)
        full_summary = summary_match.group(1).strip() if summary_match else "No summary available."
        
        # Calculate Risk Level based on extracted fields
        risk_level = "Low"
        if "Critical" in sensitivity or "High" in sensitivity:
             risk_level = "High" if "Critical" in forensic_value else "Medium"
        elif "High" in forensic_value:
             risk_level = "Medium"
        
        # Refine Risk Level
        if "Critical" in forensic_value:
            risk_level = "High"
        elif "High" in sensitivity:
            risk_level = "High"
        elif "Medium" in sensitivity or "Medium" in forensic_value:
             risk_level = "Medium"
        else:
             risk_level = "Low"

        # The summary preview
        summary_preview = full_summary[:200] + "..." if len(full_summary) > 200 else full_summary

        # --- Enhanced Parsing: Findings Table ---
        findings = []
        # Regex to find the markdown table rows after the Findings header
        # We look for lines starting with | and containing |
        # Context: ### 5.2 Suspicious or High-Risk Findings ... \n | Finding | Security Implication | \n |:--|:--|
        table_section = re.search(r"### 5\.2 Suspicious or High-Risk Findings.*?\n((?:\|.*\|\n)+)", content, re.DOTALL)
        if table_section:
            table_text = table_section.group(1)
            rows = table_text.strip().split('\n')
            for row in rows:
                # Skip header and separator lines
                if "Implication" in row or "---" in row:
                    continue
                
                parts = [p.strip() for p in row.split('|') if p.strip()]
                if len(parts) >= 2:
                    # Clean up bold markers
                    finding_text = parts[0].replace("**", "")
                    implication_text = parts[1].replace("**", "")
                    findings.append(Finding(finding=finding_text, implication=implication_text))

        return ReportMetadata(
            filename=filename,
            title=title,
            risk_level=risk_level,
            forensic_value=forensic_value,
            sensitivity=sensitivity,
            summary_preview=summary_preview,
            findings=findings
        )
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Forensic Dashboard Backend is running"}

@app.get("/reports", response_model=List[ReportMetadata])
def get_reports():
    results = []
    if os.path.exists(REPORTS_DIR):
        for f in os.listdir(REPORTS_DIR):
            if f.endswith(".md"):
                meta = parse_md_file(os.path.join(REPORTS_DIR, f))
                if meta:
                    results.append(meta)
    return results

@app.get("/reports/{filename}")
def get_report_content(filename: str):
    file_path = os.path.join(REPORTS_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Report not found")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return {"filename": filename, "content": content}

@app.get("/stats", response_model=Stats)
def get_stats():
    reports = get_reports()
    high = sum(1 for r in reports if r.risk_level == "High" or r.risk_level == "Critical")
    medium = sum(1 for r in reports if r.risk_level == "Medium")
    low = sum(1 for r in reports if r.risk_level == "Low")
    
    # Calculate total findings across all reports
    total_findings = 0
    for r in reports:
        total_findings += len(r.findings)

    return Stats(
        total_files=len(reports),
        high_risk_count=high,
        medium_risk_count=medium,
        low_risk_count=low,
        critical_findings_count=total_findings
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
