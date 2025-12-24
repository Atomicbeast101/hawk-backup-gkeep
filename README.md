# HawkBackup - Google Keep Backup

Simple Ansible playbook to backup data from Google Keep via API.

## Requirements

* Google account that was used for Google Keep
* Master token to use for Google Keep API. More details can be found [here](https://gkeepapi.readthedocs.io/en/latest/#obtaining-a-master-token).

Here's a quick guide on how to get the master token:
1) Open terminal and run this command (if you have Docker installed already):
```bash
docker run --rm -it --entrypoint /bin/sh python:3 -c 'pip install gpsoauth; python3 -c '\''print(__import__("gpsoauth").exchange_token(input("Email: "), input("OAuth Token: "), input("Android ID: ")))'\'
```
2) Leave that terminal open, open a browser, go to [https://accounts.google.com/EmbeddedSetup](https://accounts.google.com/EmbeddedSetup) and login using your Google account that is used for Google Keep. Then click on "I Agree" blue button.
3) Loading page will get stuck at loading forever which is expected. You will need to access the cookies data and retrieve `oauth_token` value. Once you do, go back to the terminal and use that value to answer `OAuth Token: ` after putting in the same email you used to login for `Email: `. `Android ID: ` should be set to `0123456789abcdef`.
4) A JSON output will be generated, look for `Token` value. That's the master token to use for `GOOGLE_KEEP_MASTER_TOKEN` env variable.

## How it Works

Whenever the cron schedule hits, it runs an Ansible playbook that does the following:
1) Create `/app/.downloads` folder.
2) Run `extract.py` Python script to download all notes via API from Google Keep.
3) Uploads that extracted data file to SFTP endpoint.
5) Removes the data file from `/app/.downloads`.
6) Checks SFTP endpoint for any old backups to remove.

This uses [gkeepapi](https://github.com/kiwiz/gkeepapi) which is a 3rd-party unofficial Python package that leverages Android API endpoint to pull notes. Using Google Keep API with its official authentication method requires a Google Workspace account which costs money. Please expect that this can break if Google decides to change that old authentication.

If any of the tasks above fails, a Pushover notification will be sent stating that the backup failed.

## Setup - Docker

Here's an example of how to run this application in Docker:

```bash
docker run \
    -e GOOGLE_KEEP_ACCOUNT=example@gmail.com \
    -e GOOGLE_KEEP_MASTER_TOKEN=<master_token> \
    -e SFTP_HOST=sftp.example.com \
    -e SFTP_USERNAME=backup \
    -e SFTP_PASSWORD=<password> \
    -e SFTP_PATH="/path/to/directory" \
    -e PUSHOVER_USER_KEY=<user_key> \
    -e PUSHOVER_APP_TOKEN=<user_password> \
    ghcr.io/atomicbeast101/hawk-backup-gkeep:latest
```

More details on the environment variables can be found below.

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
| BACKUP_RETENTION_IN_DAYS | # of days to keep historical backups for. | 10 |
