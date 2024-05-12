# Postmortem Report: 504 Error Incident

## Incident Report for Website Outage

![Server Error](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif)

### Summary

On May 10th, 2024, at 3:00 AM EAT (East Africa Time), users encountered a 504 error when attempting to access a website hosted on our server. The server operates on a LAMP stack.

### Timeline

- **03:00 AM EAT**: Users reported receiving a 500 error when accessing the website.
- **03:05 AM EAT**: Checked Apache and MySQL status and confirmed they were running.
- **03:10 AM EAT**: Website still not loading correctly, server and database functioning normally.
- **03:12 AM EAT**: Restarted Apache server, website responded with status 200 OK when accessed via curl.
- **03:18 AM EAT**: Reviewed error logs for potential issues.
- **03:25 AM EAT**: Discovered Apache server was shutting down prematurely, PHP error logs missing.
- **03:30 AM EAT**: Found PHP error logging disabled in php.ini, enabled logging.
- **03:32 AM EAT**: Restarted Apache server and checked PHP error logs.
- **03:36 AM EAT**: The PHP error log revealed a misspelled file name in wp-settings.php.
- **03:38 AM EAT**: Corrected file name and restarted Apache.
- **03:40 AM EAT**: Website resumed normal operation.

### Root Cause and Resolution

The root cause was traced to a misspelled file name referenced in wp-settings.php, causing a 500 error when accessing the server. Investigation revealed PHP error logging was disabled, hindering error identification. Enabling PHP error logging exposed the misspelling, which was promptly corrected. To prevent similar incidents, automated deployment using Puppet was implemented to ensure consistent configuration across servers.

### Corrective and Preventive Measures

- Enable error logging on all servers and websites to facilitate error identification.
- Conduct thorough testing on local environments before deploying to multi-server setups to catch errors early.
- Implement automated deployment using tools like Puppet to ensure consistent server configurations and prevent configuration errors.
