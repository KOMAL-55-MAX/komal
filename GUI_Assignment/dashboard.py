import streamlit as st
import pandas as pd
import requests
import altair as alt
import subprocess
import os
import time
import sys
from io import BytesIO

# --- API Configuration ---
API_URL = "http://127.0.0.1:8000"

def start_api_server():
    """
    Checks if the backend is running. If not, starts it.
    """
    try:
        requests.get(f"{API_URL}/", timeout=1)
        return True
    except requests.exceptions.ConnectionError:
        st.toast("⚠️ Backend offline. Initializing SOC Protocols...", icon="🔄")
        cwd = os.path.dirname(os.path.abspath(__file__))
        cmd = [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8000"]
        subprocess.Popen(cmd, cwd=cwd)
        
        for _ in range(10):
            try:
                requests.get(f"{API_URL}/", timeout=1)
                st.toast("✅ Backend Online. Systems Nominal.", icon="⚡")
                time.sleep(1)
                st.rerun()
                return True
            except requests.exceptions.ConnectionError:
                time.sleep(2)
        
        st.error("❌ CRTICAL FAILURE: Backend unreachable.")
        return False

if not start_api_server():
    st.stop()

# --- Page Config ---
st.set_page_config(
    page_title="SOC Forensic Dashboard // NGEN-X",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS (Cyberpunk/SOC Theme) ---
st.markdown("""
<style>
    /* Global Theme */
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;600;700&display=swap');
    
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(#0a1f2e 1px, transparent 1px);
        background-size: 20px 20px;
        color: #e0faff;
        font-family: 'Rajdhani', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Share Tech Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #00d9f9;
        text-shadow: 0 0 10px rgba(0, 217, 249, 0.5);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #00111a;
        border-right: 1px solid #004455;
    }
    
    /* Metrics */
    div[data-testid="metric-container"] {
        background: rgba(0, 20, 30, 0.8);
        border: 1px solid #00d9f9;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 0 15px rgba(0, 217, 249, 0.2);
        transition: all 0.3s ease;
    }
    div[data-testid="metric-container"]:hover {
        box-shadow: 0 0 25px rgba(0, 217, 249, 0.5);
        transform: translateY(-2px);
    }
    [data-testid="stMetricValue"] {
        font-family: 'Share Tech Mono', monospace;
        color: #fff;
    }

    /* Cards */
    .report-card {
        background: rgba(10, 20, 30, 0.7);
        border: 1px solid #333;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        border-left: 5px solid #555;
        transition: all 0.2s;
    }
    .report-card:hover {
        border-color: #00d9f9;
        background: rgba(0, 40, 60, 0.8);
    }
    .card-critical { border-left-color: #ff0055; animation: pulse 2s infinite; }
    .card-high { border-left-color: #ff9900; }
    .card-medium { border-left-color: #ffcc00; }
    .card-low { border-left-color: #00ff99; }

    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(255, 0, 85, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(255, 0, 85, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 0, 85, 0); }
    }

    /* Findings Table */
    .finding-row {
        padding: 10px;
        border-bottom: 1px solid #222;
        font-family: 'Rajdhani', sans-serif;
    }
    .finding-critical { color: #ff0055; font-weight: bold; }
    .finding-medium { color: #ffcc00; }
    
    /* Chart Container */
    .chart-box {
        background: rgba(0,0,0,0.3);
        border: 1px solid #004455;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- Fetch Data ---
@st.cache_data(ttl=5)
def fetch_data():
    try:
        stats = requests.get(f"{API_URL}/stats").json()
        reports = requests.get(f"{API_URL}/reports").json()
        return stats, reports
    except:
        return None, []

stats, reports = fetch_data()

# --- Header Section ---
c1, c2 = st.columns([3, 1])
with c1:
    st.title("SYS.FORENSIC // DASHBOARD_v2.0")
    st.markdown("*SECURE TERMINAL ACCESS ESTABLISHED*")
with c2:
    if st.button("🔄 REFRESH FEED"):
        st.cache_data.clear()
        st.rerun()

st.markdown("---")

# --- KPI Section (Hero) ---
if stats:
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("LOGS PROCESSED", stats.get("total_files", 0))
    k2.metric("CRITICAL THREATS", stats.get("high_risk_count", 0), delta="IMMEDIATE ACTION REQ", delta_color="inverse")
    k3.metric("WARNINGS", stats.get("medium_risk_count", 0))
    k4.metric("TOTAL FINDINGS", stats.get("critical_findings_count", 0))

# --- Main Layout ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📡 THREAT LANDSCAPE")
    
    # Graphs
    if reports:
        graph_col1, graph_col2 = st.columns(2)
        
        df = pd.DataFrame(reports)
        
        # Risk Distribution Chart
        with graph_col1:
            st.markdown("TYPE DISTRIBUTION")
            risk_counts = df['risk_level'].value_counts().reset_index()
            risk_counts.columns = ['Risk', 'Count']
            
            # Custom Cyberpunk Colors
            colors = alt.Scale(domain=['High', 'Medium', 'Low', 'Critical'], 
                             range=['#ff0055', '#ff9900', '#00ff99', '#ff0055'])
            
            chart = alt.Chart(risk_counts).mark_arc(innerRadius=60, stroke="#050505").encode(
                theta=alt.Theta("Count", stack=True),
                color=alt.Color("Risk", scale=colors),
                tooltip=["Risk", "Count"]
            ).properties(height=250)
            
            st.altair_chart(chart, use_container_width=True)

        with graph_col2:
            st.markdown("FORENSIC VALUE")
            value_chart = alt.Chart(df).mark_bar(cornerRadius=5).encode(
                x='count()',
                y=alt.Y('forensic_value', sort='-x'),
                color=alt.Color('forensic_value', scale=alt.Scale(scheme='plasma')),
                tooltip=['forensic_value', 'count()']
            ).properties(height=250)
            st.altair_chart(value_chart, use_container_width=True)

    st.subheader("📂 ARTIFACT GRID")
    
    # Reports Grid
    if reports:
        for report in reports:
            # Determine card class based on risk
            risk_class = "card-low"
            emoji = "🟢"
            if report['risk_level'] == 'Medium': 
                risk_class = "card-medium"
                emoji = "🟠"
            if report['risk_level'] in ['High', 'Critical']: 
                risk_class = "card-critical"
                emoji = "🔴"
            
            # Render custom HTML card
            st.markdown(f"""
            <div class="report-card {risk_class}">
                <div style="display:flex; justify-content:space-between;">
                    <h3>{emoji} {report['title']}</h3>
                    <span style="color:#888;">{report['filename']}</span>
                </div>
                <p><strong>RISK PROTOCOL:</strong> <span style="color:#fff;">{report['risk_level'].upper()}</span></p>
                <div style="margin-top:10px; font-size:0.9em; opacity:0.8;">
                    {report['summary_preview']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Interactive "Inject" (Button outside HTML for Streamlit event handling)
            c_view, c_dl = st.columns([1, 4])
            with c_view:
                 if st.button("ACCESS DATA", key=f"btn_{report['filename']}"):
                      # Modal
                      @st.dialog("FORENSIC DETAILED VIEW", width="large")
                      def view_report(filename):
                          try:
                              data = requests.get(f"{API_URL}/reports/{filename}").json()
                              st.markdown(data['content'])
                              st.download_button("DOWNLOAD ARTIFACT", data['content'], file_name=filename)
                          except:
                              st.error("Data corrupted.")
                      view_report(report['filename'])
            st.markdown("---")


with col_right:
    st.subheader("⚠️ INTEL FEED")
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    
    # Aggregate specific findings from all reports
    all_findings = []
    if reports:
        for r in reports:
            if 'findings' in r:
                for f in r['findings']:
                    all_findings.append({
                        "file": r['filename'],
                        "risk": r['risk_level'],
                        "what": f['finding'],
                        "why": f['implication']
                    })
    
    if all_findings:
        # Sort by risk (High/Critical first)
        all_findings.sort(key=lambda x: 0 if x['risk'] in ['High', 'Critical'] else 1)
        
        for item in all_findings:
            # Color coding
            color = "#00ff99"
            if item['risk'] == "Medium": color = "#ffcc00"
            if item['risk'] in ["High", "Critical"]: color = "#ff0055"
            
            st.markdown(f"""
            <div style="border-left: 3px solid {color}; padding-left: 10px; margin-bottom: 15px; background: rgba(0,0,0,0.5);">
                <div style="font-size: 0.8em; color: #888;">SOURCE: {item['file']}</div>
                <div style="color: {color}; font-weight: bold;">{item['what']}</div>
                <div style="font-size: 0.9em; color: #ccc;">>>> IMPLICATION: {item['why']}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No detailed intelligence findings parsed.")
        
    st.markdown('</div>', unsafe_allow_html=True)

    # Export
    st.subheader("💾 DATA EXFIL")
    if reports:
        df_exp = pd.DataFrame(reports)
        # Drop findings list for CSV clean export if needed, or keep it stringified
        csv = df_exp.drop(columns=['findings'], errors='ignore').to_csv().encode('utf-8')
        st.download_button("DOWNLOAD FULL DATASET", csv, "forensic_data.csv", "text/csv")
