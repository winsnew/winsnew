import requests
from dotenv import load_dotenv
import os

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Ambil token dari variabel lingkungan
token = os.getenv('GH_TOKEN')

if not token:
    raise ValueError("GitHub token is not set in the environment.")

# Ganti dengan username dan repository Anda
username = 'winsnew'
repo = 'winsnew'

headers = {'Authorization': f'token {token}'}

# Mengambil data commit
commits_url = f'https://api.github.com/repos/{username}/{repo}/commits'
commits_response = requests.get(commits_url, headers=headers)
commits = commits_response.json()

# Menghitung jumlah commit
commit_count = len(commits)

# Menulis data ke README.md
with open('README.md', 'r') as file:
    readme_content = file.read()

updated_readme = readme_content.replace('<!-- COMMIT_COUNT -->', str(commit_count))

with open('README.md', 'w') as file:
    file.write(updated_readme)
