from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import google.auth

SCOPES = ['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email']

def get_google_auth_url(client_secrets_file):
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
    authorization_url, state = flow.authorization_url()
    return authorization_url

def handle_google_callback(client_secrets_file, code):
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
    flow.fetch_token(code=code)
    creds = flow.credentials
    return creds