# Complete Log File Inventory

## Overview

This document provides a complete inventory of all log files analyzed in this project.

**Total Files**: 77 files
**Collection Date**: October 31, 2025, 18:50:32 UTC
**System**: DESKOFSKYCRAWLE (Windows 11 Pro Build 26200)

## File Categories

### 1. Windows Event Logs (CSV)

| File Name | Size | Description | Documentation |
|-----------|------|-------------|---------------|
| `events_filtered_Security.csv` | 1,436,860 bytes | Windows Security event log (30 days) | [Security Events](01_Event_Logs/events_filtered_Security.md) |
| `events_filtered_System.csv` | 144,316 bytes | Windows System event log | [System Events](01_Event_Logs/events_filtered_System.md) |
| `events_filtered_Application.csv` | 224,018 bytes | Windows Application event log | [Application Events](01_Event_Logs/events_filtered_Application.md) |
| `events_filtered_Microsoft-Windows-WindowsUpdateClient_Operational.csv` | 8,065 bytes | Windows Update operational events | [Update Events](01_Event_Logs/events_filtered_WindowsUpdate.md) |

### 2. Network Logs

| File Name | Size | Description | Documentation |
|-----------|------|-------------|---------------|
| `firewall_rules.csv` | 86,136 bytes | Windows Firewall rules (695 rules) | [Firewall Rules](02_Network_Logs/firewall_rules.md) |
| `firewall_profiles.txt` | 399 bytes | Firewall profile status | [Firewall Profiles](02_Network_Logs/firewall_profiles.md) |
| `netstat_ano.txt` | 9,282 bytes | Active network connections | [Network Connections](02_Network_Logs/netstat_ano.md) |
| `net_adapters.txt` | 381 bytes | Network adapters configuration | [Network Adapters](02_Network_Logs/net_adapters.md) |
| `net_ip_addresses.txt` | 499 bytes | IP address configuration | [IP Addresses](02_Network_Logs/net_ip_addresses.md) |
| `ipconfig_all.txt` | 2,465 bytes | Complete IP configuration | [IP Config](02_Network_Logs/ipconfig_all.md) |
| `route_print.txt` | 2,244 bytes | Routing table | [Routing Table](02_Network_Logs/route_print.md) |
| `arp_a.txt` | 2,412 bytes | ARP table | [ARP Table](02_Network_Logs/arp_a.md) |

### 3. System Information

| File Name | Size | Description | Documentation |
|-----------|------|-------------|---------------|
| `systeminfo.txt` | 3,200 bytes | System information summary | [System Info](03_System_Info/systeminfo.md) |
| `os_summary.txt` | 175 bytes | OS version summary | [OS Summary](03_System_Info/os_summary.md) |
| `installed_software.csv` | 7,773 bytes | Installed software list | [Installed Software](03_System_Info/installed_software.md) |
| `installed_hotfixes.txt` | 697 bytes | Windows hotfixes installed | [Hotfixes](03_System_Info/installed_hotfixes.md) |
| `services_running.csv` | 17,947 bytes | Running services list | [Services](03_System_Info/services_running.md) |
| `scheduled_tasks_verbose.txt` | 568,533 bytes | Scheduled tasks details | [Scheduled Tasks](03_System_Info/scheduled_tasks_verbose.md) |
| `local_admins.csv` | 96 bytes | Local administrator accounts | [Local Admins](03_System_Info/local_admins.md) |
| `local_users_passwordinfo.csv` | 252 bytes | Local user accounts and password info | [Local Users](03_System_Info/local_users_passwordinfo.md) |
| `bios.txt` | 144 bytes | BIOS information | [BIOS Info](03_System_Info/bios.md) |
| `volumes.txt` | 806 bytes | Disk volumes information | [Volumes](03_System_Info/volumes.md) |

### 4. Security Audit

| File Name | Size | Description | Documentation |
|-----------|------|-------------|---------------|
| `defender_status.txt` | 219 bytes | Windows Defender status | [Defender Status](04_Security_Audit/defender_status.md) |
| `defender_preferences.txt` | 8,347 bytes | Windows Defender preferences | [Defender Preferences](04_Security_Audit/defender_preferences.md) |
| `bitlocker_status.txt` | 1,495 bytes | BitLocker encryption status | [BitLocker Status](04_Security_Audit/bitlocker_status.md) |
| `cmdkey_list.txt` | 802 bytes | Stored credentials (cmdkey) | [Stored Credentials](04_Security_Audit/cmdkey_list.md) |
| `edr_candidates_present.txt` | 10 bytes | EDR detection | [EDR Detection](04_Security_Audit/edr_candidates_present.md) |
| `security_audit/process_creation_audit.csv` | Varies | Process creation events | [Process Audit](04_Security_Audit/process_creation_audit.md) |

### 5. Persistence Mechanisms

| File Name | Size | Description | Documentation |
|-----------|------|-------------|---------------|
| `persistence/registry_run_keys.csv` | Varies | Registry Run keys | [Registry Run Keys](05_Persistence/registry_run_keys.md) |
| `persistence/non_microsoft_scheduled_tasks.csv` | Varies | Non-Microsoft scheduled tasks | [Non-MS Tasks](05_Persistence/non_microsoft_scheduled_tasks.md) |
| `persistence/non_standard_services.csv` | Varies | Non-standard services | [Non-Standard Services](05_Persistence/non_standard_services.md) |
| `persistence/startup_folder_files.csv` | Varies | Startup folder files | [Startup Folders](05_Persistence/startup_folder_files.md) |
| `persistence/wmi_event_consumers.csv` | Varies | WMI event consumers | [WMI Consumers](05_Persistence/wmi_event_consumers.md) |
| `persistence/wmi_event_filters.csv` | Varies | WMI event filters | [WMI Filters](05_Persistence/wmi_event_filters.md) |
| `persistence/wmi_filter_bindings.csv` | Varies | WMI filter bindings | [WMI Bindings](05_Persistence/wmi_filter_bindings.md) |

### 6. Risk Signals

| File Name | Size | Description | Documentation |
|-----------|------|-------------|---------------|
| `risk_signals/failed_logins.csv` | Varies | Failed login attempts | [Failed Logins](06_Risk_Signals/failed_logins.md) |
| `risk_signals/successful_logins_interactive.csv` | Varies | Successful interactive logins | [Successful Logins](06_Risk_Signals/successful_logins_interactive.md) |
| `risk_signals/powershell_operational_filtered.csv` | Varies | PowerShell operational events | [PowerShell Events](06_Risk_Signals/powershell_operational_filtered.md) |
| `risk_signals/usb_disks.csv` | Varies | USB device history | [USB Devices](06_Risk_Signals/usb_disks.md) |
| `risk_signals/print_jobs.csv` | Varies | Print job history | [Print Jobs](06_Risk_Signals/print_jobs.md) |
| `risk_signals/recent_documents.csv` | Varies | Recent documents accessed | [Recent Documents](06_Risk_Signals/recent_documents.md) |
| `risk_signals/prefetch_listing.csv` | Varies | Prefetch files | [Prefetch Files](06_Risk_Signals/prefetch_listing.md) |
| `risk_signals/startup_commands.csv` | Varies | Startup commands | [Startup Commands](06_Risk_Signals/startup_commands.md) |
| `risk_signals/rdp_lsm_filtered.csv` | Varies | RDP logon events | [RDP Events](06_Risk_Signals/rdp_lsm_filtered.md) |
| `risk_signals/errors.txt` | Varies | Error logs | [Errors](06_Risk_Signals/errors.md) |

### 7. Browser Analysis

| File Name | Size | Description | Documentation |
|-----------|------|-------------|---------------|
| `browsers/Chrome/Default/extensions.csv` | Varies | Chrome extensions | [Chrome Extensions](07_Browser_Analysis/chrome_extensions.md) |
| `browsers/Chrome/Default/History_copy.db` | Varies | Chrome browsing history (SQLite) | [Chrome History](07_Browser_Analysis/chrome_history.md) |
| `browsers/Edge/Default/*.csv` | Varies | Edge extensions | [Edge Extensions](07_Browser_Analysis/edge_extensions.md) |
| `browsers/Edge/Default/*.db` | Varies | Edge browsing history (SQLite) | [Edge History](07_Browser_Analysis/edge_history.md) |

### 8. Network Analysis

| File Name | Size | Description | Documentation |
|-----------|------|-------------|---------------|
| `network_analysis/active_connections.csv` | Varies | Active network connections | [Active Connections](08_Network_Analysis/active_connections.md) |
| `network_analysis/dns_cache.csv` | Varies | DNS cache entries | [DNS Cache](08_Network_Analysis/dns_cache.md) |
| `network_analysis/hosts_file.txt` | Varies | Hosts file contents | [Hosts File](08_Network_Analysis/hosts_file.md) |
| `network_analysis/smb_shares.csv` | Varies | SMB shares configuration | [SMB Shares](08_Network_Analysis/smb_shares.md) |
| `network_analysis/wifi_profiles.csv` | Varies | WiFi profiles stored | [WiFi Profiles](08_Network_Analysis/wifi_profiles.md) |
| `network_analysis/errors.txt` | Varies | Network analysis errors | [Network Errors](08_Network_Analysis/errors.md) |

### 9. Additional Files

| File Name | Size | Description | Documentation |
|-----------|------|-------------|---------------|
| `run_metadata.json` | 225 bytes | Collection metadata | [Metadata](run_metadata.md) |
| `collector_runlog.txt` | 5,724 bytes | Collection tool log | [Collector Log](collector_runlog.md) |
| `collector_script.ps1` | 559 bytes | Collection PowerShell script | [Collector Script](collector_script.md) |
| `powershell_history.txt` | 697 bytes | PowerShell command history | [PowerShell History](powershell_history.md) |
| `transcript.txt` | 1,254 bytes | PowerShell transcript | [Transcript](transcript.md) |
| `evtx_export_skipped.txt` | 45 bytes | Skipped EVTX exports | [EVTX Skipped](evtx_export_skipped.md) |
| `gpresult.html` | 159,984 bytes | Group Policy results | [Group Policy](gpresult.md) |

## File Type Distribution

- **CSV Files**: 28 files
- **TXT Files**: 25 files
- **DB Files**: 8+ files (SQLite databases)
- **JSON Files**: 1 file
- **HTML Files**: 1 file
- **PS1 Files**: 1 file
- **SQB Files**: 1+ file (SQLite backup)

## Quick Navigation

- [Event Logs Analysis](01_Event_Logs/)
- [Network Logs Analysis](02_Network_Logs/)
- [System Information](03_System_Info/)
- [Security Audit](04_Security_Audit/)
- [Persistence Analysis](05_Persistence/)
- [Risk Signals](06_Risk_Signals/)
- [Browser Analysis](07_Browser_Analysis/)
- [Network Analysis](08_Network_Analysis/)

## Notes

- All timestamps are in the system's local timezone (UTC+05:30)
- CSV files use UTF-8 encoding with quoted fields
- Database files are SQLite 3 format
- Some files may be empty or contain minimal data
