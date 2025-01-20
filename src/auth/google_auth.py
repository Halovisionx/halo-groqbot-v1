from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import google.auth

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
def get_google_auth_url(client_secrets_file):
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
    auth_url, _ = flow.authorization_url(prompt='consent')
    return auth_url

def handle_google_callback(client_secrets_file, code):
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
    flow.fetch_token(code=code)
    creds = flow.credentials
    return creds

client_secrets_file = '/workspace/src/auth/client_secret.json'