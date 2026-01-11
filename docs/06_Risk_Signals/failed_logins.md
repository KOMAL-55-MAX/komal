# Failed Login Attempts Analysis

## File Overview

- **File Name**: `risk_signals/failed_logins.csv`
- **File Type**: CSV (Comma-Separated Values)
- **Source**: Windows Security Event Log (Event ID 4625)
- **Time Range**: 30 days (from collection date)
- **Collection Date**: October 31, 2025
- **File Size**: Varies (based on failed login count)

## Purpose

This file contains extracted failed login attempts from the Windows Security Event Log. Failed login attempts (Event ID 4625) are critical security indicators as they can indicate brute force attacks, account enumeration, or credential theft attempts.

## Structure and Fields

### CSV Format
- **Encoding**: UTF-8
- **Delimiter**: Comma (`,`)
- **Quote Character**: Double quotes (`"`)
- **Header Row**: Yes

### Fields

| Field Name | Type | Description |
|------------|------|-------------|
| `TimeCreated` | DateTime | Timestamp when the failed login occurred |
| `Id` | Integer | Event ID (4625 = Failed logon attempt) |
| `Account` | String | Account name that failed to logon |
| `WorkstationName` | String | Workstation name from which login was attempted |
| `IPAddress` | String | IP address from which login was attempted |

## Sample Data

```
TimeCreated: 30-10-2025 03:22:50 PM
Id: 4625
Account: -
WorkstationName: -
IPAddress: 127.0.0.1
```

## Analysis

### Failed Login Summary

Based on the sample data:
- **Total Failed Logins**: 1 detected
- **Source IP**: 127.0.0.1 (localhost)
- **Account**: Not specified (-)
- **Time**: October 30, 2025, 3:22:50 PM

### Security Assessment

**Low Volume**: Only 1 failed login attempt detected in 30-day period

**Analysis**:
- ✅ **GOOD**: Very low number of failed login attempts
- ⚠️ **NOTE**: Localhost (127.0.0.1) source suggests local authentication attempt
- May be from a scheduled task, service, or application authentication failure
- Single failed attempt is not necessarily malicious

## Security Relevance

### Use Cases

1. **Brute Force Detection**
   - Multiple failed logins from same source: Brute force attack
   - Failed logins to multiple accounts: Account enumeration
   - Failed logins from unexpected locations: Credential theft

2. **Account Compromise Indicators**
   - Failed logins followed by successful login: Potential compromise
   - Failed logins to administrator accounts: Targeted attack
   - Failed logins outside business hours: Suspicious activity

3. **Incident Investigation**
   - Identify attack patterns
   - Determine attack source
   - Correlate with other security events

4. **Security Monitoring**
   - Monitor for brute force attacks
   - Detect account enumeration attempts
   - Identify credential theft attempts

### Key Security Indicators

1. **Low Failed Login Count**
   - ✅ Good: Low number indicates no active brute force attacks
   - Normal system behavior expected
   - Single localhost attempt is likely benign

2. **Localhost Source (127.0.0.1)**
   - Suggests local authentication attempt
   - May be from scheduled task or service
   - Less concerning than external source

3. **Account Not Specified**
   - Account field is "-" (not populated)
   - May indicate service account authentication failure
   - Should correlate with other events

## Security Recommendations

1. **Monitoring**
   - Set up alerts for multiple failed login attempts
   - Monitor for failed logins to administrator accounts
   - Track failed logins from external sources

2. **Thresholds**
   - Alert after 5 failed logins from same source
   - Alert on failed logins to admin accounts
   - Alert on failed logins from external IPs

3. **Investigation**
   - Correlate with successful logins
   - Check for related security events
   - Review authentication logs

4. **Prevention**
   - Implement account lockout policies
   - Use strong passwords
   - Enable multi-factor authentication where possible

## Potential Threats

1. **Brute Force Attacks**
   - Multiple failed logins from same source
   - Sequential login attempts
   - Password guessing attempts

2. **Account Enumeration**
   - Failed logins to multiple accounts
   - Testing for valid account names
   - Preparing for targeted attack

3. **Credential Theft**
   - Failed logins from unexpected locations
   - Failed logins using stolen credentials
   - Attempts from compromised systems

## Related Files

- `events_filtered_Security.csv` - Full Security Event Log (includes all 4625 events)
- `risk_signals/successful_logins_interactive.csv` - Successful interactive logins
- `local_admins.csv` - Administrator accounts (high-value targets)
- `local_users_passwordinfo.csv` - User account information

## Notes

- Event ID 4625 indicates failed logon attempt
- Low failed login count is positive security indicator
- Localhost source (127.0.0.1) suggests local authentication attempt
- Should be monitored and correlated with other security events
- Account lockout policies can prevent brute force attacks
