# Security Event Log Analysis

## File Overview

- **File Name**: `events_filtered_Security.csv`
- **File Type**: CSV (Comma-Separated Values)
- **Source**: Windows Security Event Log (Event Viewer)
- **Time Range**: 30 days (Last 30 days from collection date)
- **Collection Date**: October 31, 2025, 18:50:32 UTC
- **File Size**: 1,436,860 bytes (~1.4 MB)
- **Record Count**: ~40,000 entries (estimated)

## Purpose

This file contains Windows Security Event Log entries filtered from the last 30 days. Security Event Logs are critical for security monitoring as they record authentication, authorization, account management, privilege use, and system events.

## Structure and Fields

### CSV Format
- **Encoding**: UTF-8
- **Delimiter**: Comma (`,`)
- **Quote Character**: Double quotes (`"`)
- **Header Row**: Yes

### Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `TimeCreated` | DateTime | Timestamp when the event occurred (Format: "DD-MM-YYYY HH:MM:SS AM/PM") |
| `Id` | Integer | Windows Event ID (unique identifier for event type) |
| `LevelDisplayName` | String | Event severity level (Information, Warning, Error, Critical, Verbose) |
| `Message` | Text | Detailed event message with event-specific data |

## Important Event IDs

Common security event IDs found in Windows Security logs:

### Authentication Events
- **4624**: Successful logon
- **4625**: Failed logon attempt
- **4648**: Logon with explicit credentials
- **4672**: Special privileges assigned to new logon
- **4647**: User initiated logoff
- **4634**: Account was logged off

### Account Management
- **4720**: User account was created
- **4722**: User account was enabled
- **4724**: Attempt to reset account password
- **4726**: User account was deleted
- **4732**: Member was added to a security-enabled local group
- **4733**: Member was removed from a security-enabled local group

### Privilege Use
- **4672**: Special privileges assigned to new logon
- **4673**: Sensitive privilege use
- **4674**: Operation attempted on privileged object

### System Events
- **4608**: Windows is starting up
- **4609**: Windows is shutting down
- **4616**: System time was changed

## Sample Entry Analysis

```
"TimeCreated": "31-10-2025 06:50:22 PM"
"Id": "4672"
"LevelDisplayName": "Information"
"Message": "Special privileges assigned to new logon.

Subject:
	Security ID:		S-1-5-18
	Account Name:		SYSTEM
	Account Domain:		NT AUTHORITY
	Logon ID:		0x3E7

Privileges:		SeAssignPrimaryTokenPrivilege
			SeTcbPrivilege
			SeSecurityPrivilege
			[... additional privileges ...]"
```

### Analysis:
- **Event ID 4672**: Special privileges assigned to new logon
- **Subject**: SYSTEM account (S-1-5-18) - This is the Windows Local System account
- **Privileges**: Multiple high-level privileges assigned including:
  - SeTcbPrivilege (Act as part of the operating system)
  - SeDebugPrivilege (Debug programs)
  - SeSecurityPrivilege (Manage auditing and security log)
  - SeBackupPrivilege / SeRestorePrivilege

**Security Relevance**: This is a normal system event when services or system processes start. However, if seen with unexpected accounts, it could indicate privilege escalation.

## Security Relevance

### Use Cases

1. **Incident Investigation**
   - Track failed authentication attempts (Event ID 4625)
   - Identify successful logons from unusual locations or times (Event ID 4624)
   - Detect privilege escalation attempts (Event ID 4672)

2. **Compliance and Auditing**
   - Account management activities (creation, deletion, password changes)
   - Access to sensitive resources
   - Policy violations

3. **Threat Detection**
   - Brute force attacks (multiple 4625 events)
   - Lateral movement (logons from internal systems)
   - Privilege abuse (unusual privilege use)

4. **Forensic Analysis**
   - Timeline reconstruction
   - User activity tracking
   - System access patterns

### Key Security Indicators

1. **Failed Logon Attempts (4625)**
   - Multiple failed logons from same source: Brute force attack
   - Failed logons to multiple accounts: Account enumeration
   - Failed logons from unexpected locations: Credential theft

2. **Privilege Escalation (4672)**
   - Non-administrative accounts with administrative privileges: Potential compromise
   - Unexpected privilege assignments: Malicious activity

3. **Account Management Events**
   - New administrative accounts: Potential backdoor creation
   - Password resets on privileged accounts: Account compromise
   - Account deletions: Attempt to hide tracks

## Log Patterns

### Normal Patterns
- Regular logon/logoff events during business hours
- System account (S-1-5-18) privilege assignments during system startup
- Service account authentications
- Scheduled task executions

### Suspicious Patterns
- Failed logon attempts outside business hours
- Multiple failed logons followed by successful logon (brute force success)
- Logons from geographically impossible locations
- Privilege assignments to non-administrative accounts
- Account creation/deletion outside normal business hours

## Time Range Analysis

**Coverage**: Last 30 days from October 31, 2025
- **Earliest Event**: Approximately September 30, 2025
- **Latest Event**: October 31, 2025

## Potential Threats and Anomalies

Based on the file structure and common security event patterns:

1. **Brute Force Attacks**: Look for Event ID 4625 with multiple failed attempts
2. **Privilege Escalation**: Monitor Event ID 4672 for unexpected accounts
3. **Account Compromise**: Track Event ID 4648 (logon with explicit credentials)
4. **Lateral Movement**: Monitor Event ID 4624 for logons from internal systems
5. **Persistence**: Check for Event ID 4720 (account creation) or 4732 (group membership changes)

## Recommendations

1. **Regular Monitoring**: Review security logs regularly for anomalies
2. **Alerting**: Set up alerts for:
   - Multiple failed logon attempts (4625)
   - New administrative accounts (4720 + group membership)
   - Privilege escalation (4672) on non-system accounts
   - Logons outside business hours
3. **Retention**: Maintain appropriate log retention policies
4. **Centralized Logging**: Consider forwarding logs to SIEM systems

## Related Files

- `events_filtered_System.csv` - System-level events
- `events_filtered_Application.csv` - Application-level events
- `risk_signals/failed_logins.csv` - Extracted failed login attempts
- `risk_signals/successful_logins_interactive.csv` - Successful interactive logons

## Notes

- CSV format requires careful parsing due to multiline messages
- Event messages contain structured data that may need specialized parsing
- Timezone: Events are recorded in system local time (UTC+05:30)
- File size suggests comprehensive logging is enabled
