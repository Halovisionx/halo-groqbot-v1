# src/main.py
import os
from dotenv import load_dotenv
import streamlit as st
from src.user_auth import display_auth_ui
from src.github_auth import get_github_auth_url, handle_github_callback
from src.google_auth import get_google_auth_url, handle_google_callback
from src.chat.chat_history import display_chat_ui, init_db

# Load environment variables from .env file
load_dotenv()

def main():
    st.set_page_config(page_icon="💬", layout="wide", page_title="My Streamlit App")
    init_db()  # Initialize the database
    st.title("My Streamlit App")
    display_auth_ui()

    # Debug prints
    st.write(f"GOOGLE_CLIENT_SECRET: {os.getenv('GOOGLE_CLIENT_SECRET')}")
    st.write(f"GITHUB_CLIENT_ID: {os.getenv('GITHUB_CLIENT_ID')}")
    st.write(f"GITHUB_CLIENT_SECRET: {os.getenv('GITHUB_CLIENT_SECRET')}")

    # GitHub Authentication
    github_client_id = os.getenv('GITHUB_CLIENT_ID')
    github_client_secret = os.getenv('GITHUB_CLIENT_SECRET')
    github_redirect_uri = 'http://localhost:8501/callback'
    github_auth_url = get_github_auth_url(github_client_id, github_redirect_uri)
    st.write(f'Please go <a href="{github_auth_url}">here</a> and authorize access.', unsafe_allow_html=True)

    code = st.experimental_get_query_params().get('code')
    if code:
        token = handle_github_callback(github_client_id, github_client_secret, github_redirect_uri, code[0])
        st.write(f'GitHub token: {token}')

    # Google Authentication
    google_client_secrets_file = 'src/auth/client_secret.json'  # Updated path
    google_auth_url = get_google_auth_url(google_client_secrets_file)
    st.write(f'Please go <a href="{google_auth_url}">here</a> and authorize access.', unsafe_allow_html=True)

    code = st.experimental_get_query_params().get('code')
    if code:
        creds = handle_google_callback(code[0])
        st.write(f'Google credentials: {creds}')

    # Display Chat UI
    display_chat_ui()