# Cybersecurity Log Analysis & Documentation

## Project Overview

This repository contains a comprehensive analysis of cybersecurity log files collected from a Windows 11 Pro system audit. The logs were collected using VOLDEBUG (Volume Debug) audit tool on October 31, 2025, covering a 30-day period of system, network, and security events.

## System Information

- **Hostname**: DESKOFSKYCRAWLE
- **OS**: Microsoft Windows 11 Pro (Build 26200)
- **Architecture**: 64-bit
- **User**: Bharat (MIS)
- **Auditor**: Meet
- **Collection Date**: October 31, 2025, 18:50:32 UTC
- **Audit Period**: 30 days
- **Last Boot**: October 31, 2025, 11:34:24 AM

## Repository Structure

```
.
├── README.md                 # This file - Project overview and navigation
├── docs/                     # Detailed documentation for each log file
│   ├── 00_Index.md           # Complete file inventory and navigation
│   ├── 01_Event_Logs/        # Windows Event Log analysis (Security, System, Application)
│   ├── 02_Network_Logs/      # Network analysis (firewall, connections, DNS)
│   ├── 03_System_Info/       # System configuration and installed software
│   ├── 04_Security_Audit/    # Security configurations and status
│   ├── 05_Persistence/       # Persistence mechanisms analysis
│   ├── 06_Risk_Signals/      # Security risk indicators
│   ├── 07_Browser_Analysis/  # Browser history and extensions
│   └── 08_Network_Analysis/  # Network analysis subdirectory
├── logs/                     # Original log files (CSV, TXT, DB formats)
└── scripts/                  # Analysis scripts and utilities
```

## Log Files Summary

### Total Files Analyzed: 77

The logs include:
- **Windows Event Logs** (CSV): Security, System, Application events (40,000+ entries)
- **Network Logs** (CSV/TXT): Firewall rules, active connections, DNS cache, SMB shares
- **System Information** (CSV/TXT): Installed software, services, scheduled tasks, user accounts
- **Security Audit** (TXT/CSV): Windows Defender status, BitLocker status, process creation events
- **Persistence Mechanisms** (CSV): Registry run keys, scheduled tasks, WMI events
- **Risk Signals** (CSV/TXT): Failed logins, PowerShell operations, USB devices, print jobs
- **Browser Data** (DB/CSV): Chrome and Edge history databases, extensions
- **Network Analysis** (CSV/TXT): Active connections, DNS cache, hosts file, WiFi profiles

## Executive Summary

For a comprehensive summary of findings and recommendations, see [**Executive Summary**](docs/SUMMARY.md).

## Key Findings Summary

### Security Status
- ✅ **Windows Defender**: Enabled (Real-time protection active)
- ✅ **BitLocker**: Enabled on C: and D: drives (Volume E: unprotected)
- ⚠️ **Failed Login Attempts**: 1 detected from localhost (127.0.0.1)
- ⚠️ **Remote Desktop**: Potential RDP activity detected
- ⚠️ **AnyDesk**: Remote access software installed

### Network Security
- **Firewall**: Multiple rules configured (695 rules)
- **Active Connections**: Various services listening on network interfaces
- **SMB Shares**: File sharing services active
- **WiFi Profiles**: Multiple network profiles stored

### System Configuration
- **Local Administrators**: 2 accounts (Administrator, Dell)
- **Running Services**: 200+ services (includes AnyDesk)
- **Installed Software**: 30+ applications including development tools
- **Scheduled Tasks**: Multiple automated tasks configured

### Persistence Mechanisms
- **Registry Run Keys**: 13 entries (HKLM and HKCU)
- **Non-Microsoft Scheduled Tasks**: Detected
- **Startup Folders**: Files present
- **WMI Event Consumers**: Configured

## Documentation Navigation

Detailed analysis for each log file can be found in the `docs/` directory:

1. **[Complete File Index](docs/00_Index.md)** - Inventory of all 77 files
2. **[Event Logs Documentation](docs/01_Event_Logs/)** - Windows Event Log analysis
3. **[Network Logs Documentation](docs/02_Network_Logs/)** - Firewall and network activity
4. **[System Information](docs/03_System_Info/)** - Software, services, users
5. **[Security Audit](docs/04_Security_Audit/)** - Defender, BitLocker, process audit
6. **[Persistence Analysis](docs/05_Persistence/)** - Persistence mechanisms
7. **[Risk Signals](docs/06_Risk_Signals/)** - Security indicators and anomalies
8. **[Browser Analysis](docs/07_Browser_Analysis/)** - Browser history and extensions
9. **[Network Analysis](docs/08_Network_Analysis/)** - Network configuration details

## Tools Used

- **VOLDEBUG** - Windows security audit collection tool
- **Python** - Log analysis and processing (if scripts provided)
- **PowerShell** - Initial file processing
- **SQLite** - Browser database analysis (if needed)

## Security Relevance

This log collection is valuable for:
- **Threat Detection**: Identifying suspicious activities and anomalies
- **Incident Response**: Timeline reconstruction and attack analysis
- **Security Auditing**: Compliance and security posture assessment
- **Forensic Investigation**: Understanding system state and user activities
- **Baseline Establishment**: Normal behavior identification

## Important Security Notes

1. **Sensitive Data**: This repository may contain sensitive system information. Exercise caution when sharing.
2. **IP Addresses**: Real IP addresses and hostnames are present in the logs.
3. **User Data**: Browser history and user activities are documented.
4. **Credentials**: No plaintext passwords are stored, but authentication patterns are visible.

## Analyst Information

- **Analyst**: [Your Name]
- **Date**: January 11, 2026
- **Purpose**: Cybersecurity log analysis and documentation assignment

## License

This documentation is provided for educational and security analysis purposes.
