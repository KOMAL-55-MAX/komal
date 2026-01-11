# Registry Run Keys Analysis

## File Overview

- **File Name**: `persistence/registry_run_keys.csv`
- **File Type**: CSV (Comma-Separated Values)
- **Source**: Windows Registry (Run and RunOnce keys)
- **Time Range**: Current configuration at time of collection
- **Collection Date**: October 31, 2025
- **File Size**: Varies
- **Record Count**: 13 entries

## Purpose

This file contains entries from Windows Registry Run and RunOnce keys. These registry keys are used to automatically start programs when a user logs on or the system starts. They are critical persistence mechanisms that attackers often abuse to maintain access.

## Structure and Fields

### CSV Format
- **Encoding**: UTF-8
- **Delimiter**: Comma (`,`)
- **Quote Character**: Double quotes (`"`)
- **Header Row**: Yes

### Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `RegistryKey` | String | Full registry key path (HKLM or HKCU) |
| `Name` | String | Entry name within the registry key |
| `Value` | String | Command/executable path to run |

## Registry Keys Analyzed

1. **HKLM:\Software\Microsoft\Windows\CurrentVersion\Run**
   - System-wide startup programs
   - Runs for all users
   - Higher privileges

2. **HKCU:\Software\Microsoft\Windows\CurrentVersion\Run**
   - User-specific startup programs
   - Runs for current user only
   - Lower privileges

3. **HKCU:\Software\Microsoft\Windows\CurrentVersion\RunOnce**
   - Programs that run once per user login
   - Typically for cleanup or one-time tasks

## Sample Entries Analysis

### System-Wide Run Keys (HKLM)

#### 1. SecurityHealth
```
RegistryKey: HKLM:\Software\Microsoft\Windows\CurrentVersion\Run
Name: SecurityHealth
Value: C:\WINDOWS\system32\SecurityHealthSystray.exe
```
**Analysis**: ✅ **LEGITIMATE** - Windows Security Health system tray icon (normal Windows component)

#### 2. RtkAudUService
```
RegistryKey: HKLM:\Software\Microsoft\Windows\CurrentVersion\Run
Name: RtkAudUService
Value: "C:\WINDOWS\System32\DriverStore\FileRepository\realtekservice.inf_amd64_04ff63d068f8c626\RtkAudUService64.exe" -background
```
**Analysis**: ✅ **LEGITIMATE** - Realtek audio service (system driver, normal component)

#### 3. WavesSvc
```
RegistryKey: HKLM:\Software\Microsoft\Windows\CurrentVersion\Run
Name: WavesSvc
Value: "C:\WINDOWS\System32\DriverStore\FileRepository\wavesapo12de.inf_amd64_0dbb828df1dc4b7c\WavesSvc64.exe" -Jack
```
**Analysis**: ✅ **LEGITIMATE** - Waves audio service (audio enhancement software, normal component)

### User-Specific Run Keys (HKCU)

#### 4. MicrosoftEdgeAutoLaunch
```
RegistryKey: HKCU:\Software\Microsoft\Windows\CurrentVersion\Run
Name: MicrosoftEdgeAutoLaunch_B5BC174A7B4ABF98EC6D64B02610726A
Value: "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --win-session-start
```
**Analysis**: ✅ **LEGITIMATE** - Microsoft Edge auto-launch (browser startup, normal)

#### 5. OneDrive
```
RegistryKey: HKCU:\Software\Microsoft\Windows\CurrentVersion\Run
Name: OneDrive
Value: "C:\Users\Dell\AppData\Local\Microsoft\OneDrive\OneDrive.exe" /background
```
**Analysis**: ✅ **LEGITIMATE** - Microsoft OneDrive sync service (cloud storage, normal)

#### 6. Client Authentication Agent
```
RegistryKey: HKCU:\Software\Microsoft\Windows\CurrentVersion\Run
Name: Client Authentication Agent
Value: "C:\Users\Dell\AppData\Local\Sophos\Client Authentication Agent\CAA.exe" -a
```
**Analysis**: ✅ **LEGITIMATE** - Sophos Client Authentication Agent (security software, normal)

#### 7. Microsoft.Lists
```
RegistryKey: HKCU:\Software\Microsoft\Windows\CurrentVersion\Run
Name: Microsoft.Lists
Value: C:\Users\Dell\AppData\Local\Microsoft\OneDrive\25.212.1029.0001_1\OneDrive.Sync.Service.exe
```
**Analysis**: ✅ **LEGITIMATE** - OneDrive sync service (part of OneDrive, normal)

#### 8. Adobe Acrobat Synchronizer
```
RegistryKey: HKCU:\Software\Microsoft\Windows\CurrentVersion\Run
Name: Adobe Acrobat Synchronizer
Value: "C:\Program Files\Adobe\Acrobat DC\Acrobat\AdobeCollabSync.exe"
```
**Analysis**: ✅ **LEGITIMATE** - Adobe Acrobat collaboration sync (installed software, normal)

### RunOnce Keys (Cleanup Tasks)

#### 9-13. OneDrive Cleanup Tasks
Multiple RunOnce entries for OneDrive update cleanup:
- Delete cached update binaries
- Uninstall old OneDrive versions

**Analysis**: ✅ **LEGITIMATE** - Cleanup tasks for OneDrive updates (normal maintenance)

## Security Assessment

### Summary

**Total Entries**: 13
- **HKLM Run Keys**: 3 entries (all legitimate)
- **HKCU Run Keys**: 5 entries (all legitimate)
- **HKCU RunOnce Keys**: 5 entries (all legitimate cleanup tasks)

**Overall Status**: ✅ **GOOD** - All entries appear legitimate

### Analysis

1. **System Components**: All HKLM entries are legitimate Windows components or drivers
2. **Installed Software**: All HKCU entries are from legitimate installed software (Edge, OneDrive, Adobe, Sophos)
3. **No Suspicious Entries**: No unknown executables or suspicious paths detected
4. **RunOnce Cleanup**: RunOnce entries are normal cleanup tasks

## Security Relevance

### Use Cases

1. **Persistence Detection**
   - Identify programs that start automatically
   - Detect malware persistence mechanisms
   - Find unauthorized startup programs

2. **Incident Investigation**
   - Determine what programs start at login
   - Identify potential attack vectors
   - Track persistence mechanisms used by attackers

3. **Security Hardening**
   - Review startup programs
   - Remove unnecessary startup entries
   - Minimize attack surface

4. **Compliance Checking**
   - Verify only authorized programs start automatically
   - Ensure no unauthorized software in startup
   - Document startup programs

### Key Security Indicators

1. **Legitimate Programs**
   - ✅ All entries are from known, legitimate sources
   - ✅ Paths are in standard Windows/system directories
   - ✅ No suspicious executable names or paths

2. **RunOnce Keys**
   - ✅ RunOnce keys are used for cleanup (normal)
   - ✅ No persistent RunOnce entries (suspicious pattern)

3. **Registry Locations**
   - ✅ HKLM entries are system components (normal)
   - ✅ HKCU entries are user-installed software (normal)
   - ✅ No unusual registry paths

## Potential Threats

### Normal Patterns (Good)
- System components in HKLM Run keys
- Installed software in HKCU Run keys
- Cleanup tasks in RunOnce keys

### Suspicious Patterns (Not Found)
- Executables in user temp folders
- Unknown executable names
- Base64 encoded commands
- Scripts (PowerShell, VBScript, etc.)
- Network paths (\\server\share\file.exe)
- Suspicious paths (AppData\Roaming\random)

## Security Recommendations

1. **Regular Monitoring**
   - Review Run keys periodically
   - Compare against baseline
   - Alert on new entries

2. **Documentation**
   - Document all legitimate startup programs
   - Maintain baseline of known-good entries
   - Justify each startup entry

3. **Minimization**
   - Remove unnecessary startup programs
   - Disable software that doesn't need to start automatically
   - Reduce attack surface

4. **Monitoring**
   - Monitor registry changes to Run keys
   - Alert on new entries (Event ID 4657)
   - Track persistence mechanisms

## Related Files

- `persistence/startup_folder_files.csv` - Startup folder files
- `persistence/non_microsoft_scheduled_tasks.csv` - Scheduled tasks
- `persistence/wmi_event_consumers.csv` - WMI persistence
- `events_filtered_Security.csv` - Security events (registry changes)
- `risk_signals/startup_commands.csv` - Startup commands

## Notes

- Run keys are processed at user login
- HKLM Run keys run with SYSTEM privileges
- HKCU Run keys run with user privileges
- RunOnce keys are deleted after execution
- Changes to Run keys are logged in Security Event Log (Event ID 4657)
- Malware often uses Run keys for persistence
- Should be reviewed regularly for unauthorized entries

## Compliance Considerations

- **Least Privilege**: Only necessary programs should start automatically
- **Change Management**: Changes to startup programs should be documented
- **Monitoring**: Startup programs should be monitored and reviewed
