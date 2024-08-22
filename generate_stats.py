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
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        # Debugging: Print the raw response to check its structure
        print("Raw response:", data)
        
        # Check if 'total_count' is in the response
        if 'total_count' in data:
            return data['total_count']
        else:
            print("Key 'total_count' not found in the response.")
            return 0
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 0

if __name__ == '__main__':
    commits = get_yearly_commits(GITHUB_USERNAME, GITHUB_TOKEN)
    with open('README.md', 'r') as file:
        readme = file.readlines()

    with open('README.md', 'w') as file:
        for line in readme:
            file.write(line)
        file.write(f'\n## Yearly Contributions: {commits}\n')
