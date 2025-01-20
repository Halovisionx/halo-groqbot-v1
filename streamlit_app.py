import requests
import streamlit as st

# GitHub Personal Access Token'ı Streamlit secrets'dan alın.
github_token = st.secrets["GITHUB_TOKEN"]
organization = "YOUR_ORGANIZATION_NAME"

# GitHub API'sine istek gönder.
url = f"https://api.github.com/orgs/{organization}/repos"
headers = {
    "Authorization": f"token {github_token}"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    repos = response.json()
    st.write(f"{organization} organizasyonundaki repolar:")
    for repo in repos:
        st.write(repo["name"])
else:
    st.error("GitHub API isteği başarısız oldu.")

# Streamlit uygulamanızı çalıştırın.
if __name__ == "__main__":
    st.title("GitHub Organizasyon Repoları")
    st.text("GitHub organizasyonunuza ait repoları listelemektedir.")
