# Imports
import gkeepapi
import json
import sys
import os

# Attributes
GOOGLE_KEEP_ACCOUNT = os.environ.get('GOOGLE_KEEP_ACCOUNT')
GOOGLE_KEEP_MASTER_TOKEN = os.environ.get('GOOGLE_KEEP_MASTER_TOKEN')

# Main
try:
    api = gkeepapi.Keep()
    api.authenticate(GOOGLE_KEEP_ACCOUNT, GOOGLE_KEEP_MASTER_TOKEN)

    notes = api.dump()
    json.dump(notes, open(f".downloads/{sys.argv[1]}", 'w'))

except Exception as ex:
    raise Exception(f'Unable to access Google Keep API! Reason: {str(ex)}')
