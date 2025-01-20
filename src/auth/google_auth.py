import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def get_google_auth_url(client_secrets_file):
    client_secrets_json = json.loads(os.environ.get('GOOGLE_CLIENT_SECRET'))
    flow = InstalledAppFlow.from_client_config(client_secrets_json, SCOPES)
    auth_url, _ = flow.authorization_url(prompt='consent')
    return auth_url

def handle_google_callback(code):
    client_secrets_json = json.loads(os.environ.get('GOOGLE_CLIENT_SECRET'))
    flow = InstalledAppFlow.from_client_config(client_secrets_json, SCOPES)
    flow.fetch_token(code=code)
    creds = flow.credentials
    return creds