# HawkBackup - Google Keep Backup

Simple Ansible playbook to backup data from Google Keep via API.

## Setup

Since Google Keep API officially requires a workspace (enterprise) account in order to leverage it, this uses [gkeepapi](https://github.com/kiwiz/gkeepapi) which is an unofficial Python package that uses Android API endpoint version to pull all notes from Google Keep. Here's the guide on how to obtain the master token to use for this backup script (more details can be found [here](https://gkeepapi.readthedocs.io/en/latest/#obtaining-a-master-token)).

1) Open terminal and run this command (if you have Docker installed already):
```bash
docker run --rm -it --entrypoint /bin/sh python:3 -c 'pip install gpsoauth; python3 -c '\''print(__import__("gpsoauth").exchange_token(input("Email: "), input("OAuth Token: "), input("Android ID: ")))'\'
```
2) Leave that terminal open, open a browser, go to [https://accounts.google.com/EmbeddedSetup](https://accounts.google.com/EmbeddedSetup) and login using your Google account that is used for Google Keep. Then click on "I Agree" blue button.
3) Loading page will get stuck at loading forever which is expected. You will need to access the cookies data and retrieve `oauth_token` value. Once you do, go back to the terminal and use that value to answer `OAuth Token: ` after putting in the same email you used to login for `Email: `. `Android ID: ` should be set to `0123456789abcdef`.
4) A JSON output will be generated, look for `Token` value. That's the master token to use for `GOOGLE_KEEP_MASTER_TOKEN` env variable.

## Environment Variables

| Environment Variable | Description | Default |
| :------- | :------ | :-------: |
| GOOGLE_KEEP_ACCOUNT | Gmail user account for Google Keep API. | N/A |
| GOOGLE_KEEP_MASTER_TOKEN | Master token from the setup above. | N/A |
| SFTP_HOST | FQDN/IP address of SFTP server to send downloaded config file to. | N/A |
| SFTP_PORT | Port of SFTP server. | 22 |
| SFTP_USERNAME | Username for SFTP server. | N/A |
| SFTP_PASSWORD | Password for SFTP server. | N/A |
| SFTP_PATH | Destination path in SFTP server to store config file in. | N/A |
| PUSHOVER_USER_KEY | User key for Pushover notifications. Gets sent out for failed backups. | N/A |
| PUSHOVER_APP_TOKEN | App token for Pushover notifications. Gets sent out for failed backups. | N/A |
