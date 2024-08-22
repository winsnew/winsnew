import aiohttp
import asyncio
import os

# Ganti dengan username dan repository Anda
username = 'winsnew'
repo = 'winsnew'
token = os.getenv('GH_TOKEN')  # Menggunakan variabel lingkungan

async def fetch_commits(session):
    commits_url = f'https://api.github.com/repos/{username}/{repo}/commits'
    headers = {'Authorization': f'token {token}'}
    async with session.get(commits_url, headers=headers) as response:
        if response.status == 401:
            raise Exception("Unauthorized: Check your GitHub token.")
        response.raise_for_status()  # Memastikan status respons
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        commits = await fetch_commits(session)
        commit_count = len(commits)
        print(f'Number of commits: {commit_count}')

if __name__ == "__main__":
    asyncio.run(main())
