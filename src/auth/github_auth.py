from requests_oauthlib import OAuth2Session

def get_github_auth_url(client_id, redirect_uri):
    github = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_base_url = 'https://github.com/login/oauth/authorize'
    authorization_url, state = github.authorization_url(authorization_base_url)
    return authorization_url

def handle_github_callback(client_id, client_secret, redirect_uri, code):
    github = OAuth2Session(client_id, redirect_uri=redirect_uri)
    token_url = 'https://github.com/login/oauth/access_token'
    token = github.fetch_token(token_url, client_secret=client_secret, code=code)
    return token