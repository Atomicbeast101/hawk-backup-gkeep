#!/bin/bash

# Google Drive
export GOOGLE_API_USERNAME=atomicbrod101@gmail.com
export GOOGLE_API_SERVICE_ACCOUNT_FILE=./google_api_service_account.json

# Run python script
.venv/bin/python extract.py
