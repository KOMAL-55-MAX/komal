# Cybersecurity Forensic Dashboard
**Advanced Manual Forensic Analysis & Visualization Tool**

**Author:** Komal Shah
**Date:** January 2026

---

## 🛡️ Project Overview
This project is a comprehensive Cybersecurity Forensic Dashboard designed to assist security analysts in visualizing and analyzing forensic artifacts. It replaces automated script generation with high-fidelity **manual forensic analysis**, presenting findings through a modern, "Cyberpunk/SOC" themed interface.

The system consists of a **FastAPI backend** for parsing markdown reports and a **Streamlit frontend** for visualization, threat intelligence feeds, and data interaction.

## 🚀 Key Features

### 1. Dashboard 2.0 (Modern UI)
*   **Cyberpunk/SOC Aesthetic:** A professional dark-mode interface with neon accents, optimized for high-contrast visibility in security operations centers.
*   **Real-Time Threat Intelligence:** A dedicated "Intel Feed" that extracts and scrolls specific high-risk findings (e.g., "AnyDesk Listening", "Cleartext Wi-Fi Keys") directly from the reports.
*   **Interactive Visualizations:**
    *   **Risk Distribution Donut Chart:** Visual breakdown of High, Medium, and Low risks.
    *   **Forensic Value Bar Chart:** Metric analysis of evidence utility.
*   **Report Browser:** A responsive grid layout with "Glitch" active cards for report selection.
*   **Detailed Analysis Modal:** One-click access to full markdown reports with download capabilities.

### 2. Forensic Reporting
*   **Manual Analysis:** 13 detailed forensic reports generated from raw logs (`ipconfig`, `netstat`, `firewall`, `wifi_profiles`, etc.).
*   **Standardized Format:** All reports follow a strict structure:
    *   File Overview & Data Types
    *   Security Operations Use Cases
    *   **Suspicious Findings Table (Parsed by Backend)**
    *   Executive Summary & Risk Rating

### 3. Backend Architecture
*   **FastAPI Powered:** valid, typed, and fast API endpoints.
*   **Smart Parsing:** Custom Regex logic to extract metadata, risk levels, and specific finding tables from Markdown files.
*   **Auto-Healing:** The dashboard automatically detects if the backend is offline and spins it up.

---

## 📂 Project Structure

```
GUI_Assignment/
├── dashboard.py          # Main Streamlit Frontend Application
├── server.py             # FastAPI Backend Server & Parser
├── requirements.txt      # Python Dependencies
├── README.md             # This Documentation
├── Raw_logs/             # Source Artifacts (txt, csv)
│   ├── network_analysis/ # Subfolder for specific network logs
│   └── ...
└── Report/               # Generated Forensic Reports (.md)
    ├── Report_netstat_ano.txt.md
    ├── Report_wifi_profiles.csv.md
    └── ...
```

---

## 🛠️ Installation & Usage

### Prerequisites
*   Python 3.8+
*   Windows OS (Preferred for log context)

### 1. Setup Environment
It is recommended to use a virtual environment.
```bash
# Create virtual environment
python -m venv .venv

# Activate it
.\.venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Dashboard
You only need to run the Streamlit app. It will automatically start the backend server.
```bash
streamlit run dashboard.py
```

*The dashboard will open in your default browser at `http://localhost:8501`.*

---

## 🔍 Key Forensic Findings (Sample)

| Log Source | Finding | Risk Level |
| :--- | :--- | :--- |
| **wifi_profiles.csv** | **Cleartext Passwords** for 3 networks (WPA2/WPA3) | **CRITICAL** |
| **netstat_ano.txt** | **AnyDesk** (Remote Access Tool) listening on TCP 7070 | **HIGH** |
| **firewall_rules.csv** | Inbound Traffic allowed for AnyDesk (Public Profile) | **HIGH** |
| **active_connections** | Active session to external IP (AnyDesk) | **MEDIUM** |
| **hosts_file.txt** | No tampering detected (Clean) | **LOW** |

---

## 📜 License
This project is developed for educational and assignment purposes. All logs are simulated or sanitized.
