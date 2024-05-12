# Postmortem Report: 504 Error Incident

## Incident Report for Website Outage

![Server Error](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif)

### Summary

On May 01st, 2024, at midnight PST, users encountered a 504 error when attempting to access a website hosted on our server. The server operates on a LAMP stack.

### Timeline

- **00:00 PST**: Users reported receiving a 500 error when accessing the website.
- **00:05 PST**: Checked Apache and MySQL status, confirmed they were running.
- **00:10 PST**: Website still not loading correctly, server and database functioning normally.
- **00:12 PST**: Restarted Apache server, website responded with status 200 OK when accessed via curl.
- **00:18 PST**: Reviewed error logs for potential issues.
- **00:25 PST**: Discovered Apache server was shutting down prematurely, PHP error logs missing.
- **00:30 PST**: Found PHP error logging disabled in php.ini, enabled logging.
- **00:32 PST**: Restarted Apache server, checked PHP error logs.
- **00:36 PST**: PHP error log revealed a misspelled file name in wp-settings.php.
- **00:38 PST**: Corrected file name and restarted Apache.
- **00:40 PST**: Website resumed normal operation.

### Root Cause and Resolution

The root cause was traced to a misspelled file name referenced in wp-settings.php, causing a 500 error when accessing the server. Investigation revealed PHP error logging was disabled, hindering error identification. Enabling PHP error logging exposed the misspelling, which was promptly corrected. To prevent similar incidents, automated deployment using Puppet was implemented to ensure consistent configuration across servers.

### Corrective and Preventive Measures

- Enable error logging on all servers and websites to facilitate error identification.
- Conduct thorough testing on local environments before deploying to multi-server setups to catch errors early.
- Implement automated deployment using tools like Puppet to ensure consistent server configurations and prevent configuration errors.
