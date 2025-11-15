# HawkBackup - Google Keep Backup

Ansible playbook that backs up all notes from Google Keep via API.

## Setup

1) Run `./setup.sh` to setup the Python environment that Ansible will use to run the playbook.
2) Set the environment variables in some way (via new bash script & call ./run.sh in the end) or via DevOps pipeline.
3) Run it via DevOps pipeline or `./run.sh` directly (with environment variables set).

## Environment Variables

| Environment Variable | Description | Default |
| :------- | :------ | :-------: |
#### TODO ####
| SFTP_HOST | FQDN/IP address of SFTP server to send downloaded config file to. | N/A |
| SFTP_PORT | Port of SFTP server. | 22 |
| SFTP_USERNAME | Username for SFTP server. | N/A |
| SFTP_PASSWORD | Password for SFTP server. | N/A |
| SFTP_PATH | Destination path in SFTP server to store config file in. | N/A |
