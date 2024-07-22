import requests
from datetime import datetime
import os

GITHUB_USERNAME = 'winsnew'
GITHUB_TOKEN = os.getenv('GH_TOKEN')

def get_yearly_commits(username, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }
    url = f'https://api.github.com/search/commits?q=author:{username}+committer-date:>{datetime.now().year}-01-01'
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['total_count']

if __name__ == '__main__':
    commits = get_yearly_commits(GITHUB_USERNAME, GITHUB_TOKEN)
    with open('README.md', 'r') as file:
        readme = file.readlines()

    with open('README.md', 'w') as file:
        for line in readme:
            file.write(line)
        file.write(f'\n## Yearly Contributions: {commits}\n')
