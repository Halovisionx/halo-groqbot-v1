import streamlit as st
from src.auth.github_auth import get_github_auth_url, handle_github_callback
from src.auth.google_auth import get_google_auth_url, handle_google_callback
from src.auth.user_auth import display_auth_ui
from src.chat.chat_ui import display_chat_ui
from src.utils.helpers import icon
from src.database.db import engine, Base

# Initialize the database
Base.metadata.create_all(bind=engine)

st.set_page_config(page_icon="💬", layout="wide", page_title="Groq Goes Brrrrrrrr...")

icon("🏎️")

# User Authentication
display_auth_ui()

# GitHub Authentication
github_client_id = 'your_github_client_id'
github_client_secret = 'your_github_client_secret'
github_redirect_uri = 'http://localhost:8501/callback'

github_auth_url = get_github_auth_url(github_client_id, github_redirect_uri)
st.write(f'Please go <a href="{github_auth_url}">here</a> and authorize access.', unsafe_allow_html=True)

if st.button("Authorize GitHub"):
    # Handle the callback and get the access token
    code = st.experimental_get_query_params().get('code')
    if code:
        token = handle_github_callback(github_client_id, github_client_secret, github_redirect_uri, code[0])
        st.write(f'GitHub token: {token}')

# Google Authentication
google_client_secrets_file = 'client_secret.json'

google_auth_url = get_google_auth_url(google_client_secrets_file)
st.write(f'Please go <a href="{google_auth_url}">here</a> and authorize access.', unsafe_allow_html=True)

if st.button("Authorize Google"):
    # Handle the callback and get the credentials
    code = st.experimental_get_query_params().get('code')
    if code:
        creds = handle_google_callback(google_client_secrets_file, code[0])
        st.write(f'Google credentials: {creds}')

# Display Chat UI
display_chat_ui()