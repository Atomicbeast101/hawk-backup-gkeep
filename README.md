# HawkBackup - Google Keep Backup

Simple Ansible playbook to backup data from Google Keep via API.

## Setup



## Environment Variables

| Environment Variable | Description | Default |
| :------- | :------ | :-------: |
| GOOGLE_KEEP_ACCOUNT | Gmail account for Google API | N/A |
| GOOGLE_KEEP_MASTER_TOKEN | Master token from the setup above. | N/A |
| SFTP_HOST | FQDN/IP address of SFTP server to send downloaded config file to. | N/A |
| SFTP_PORT | Port of SFTP server. | 22 |
| SFTP_USERNAME | Username for SFTP server. | N/A |
| SFTP_PASSWORD | Password for SFTP server. | N/A |
| SFTP_PATH | Destination path in SFTP server to store config file in. | N/A |
| PUSHOVER_USER_KEY | User key for Pushover notifications. Gets sent out for failed backups. | N/A |
| PUSHOVER_APP_TOKEN | App token for Pushover notifications. Gets sent out for failed backups. | N/A |
