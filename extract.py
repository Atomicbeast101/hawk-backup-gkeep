# Imports
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os

# Attributes
GOOGLE_API_USERNAME = os.environ.get('GOOGLE_API_USERNAME')
GOOGLE_API_SERVICE_ACCOUNT_FILE = os.environ.get('GOOGLE_API_SERVICE_ACCOUNT_FILE')
SCOPES = ['https://www.googleapis.com/auth/keep']

# Main
try:
    ## Authenticate access
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_API_SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    ).with_subject(GOOGLE_API_USERNAME)
    service = build('keep', 'v1', credentials=credentials)

    ## Retrieve all notes
    results = service.notes().list().execute()
    notes = results.get('notes', [])
    print(notes)

except Exception as ex:
    raise Exception(f'Unable to access Google Keep API! Reason: {str(ex)}')
