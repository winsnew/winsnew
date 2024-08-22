import aiohttp
import asyncio
import os
from aiofiles import open as aio_open

# Ganti dengan username dan repository Anda
username = 'winsnew'
repo = 'winsnew'
token = os.getenv('GH_TOKEN')  # Mengambil token dari variabel lingkungan

# Mendapatkan data commit secara asinkron
async def fetch_commits(session):
    commits_url = f'https://api.github.com/repos/{username}/{repo}/commits'
    headers = {'Authorization': f'token {token}'}
    async with session.get(commits_url, headers=headers) as response:
        if response.status == 200:
            return await response.json()
        else:
            response.raise_for_status()

# Mengupdate README.md
async def update_readme(commit_count):
    async with aio_open('README.md', 'r') as file:
        readme_content = await file.read()
    
    updated_readme = readme_content.replace('<!-- COMMIT_COUNT -->', str(commit_count))
    
    async with aio_open('README.md', 'w') as file:
        await file.write(updated_readme)

# Main function
async def main():
    async with aiohttp.ClientSession() as session:
        commits = await fetch_commits(session)
        commit_count = len(commits)
        await update_readme(commit_count)

# Run the script
if __name__ == "__main__":
    asyncio.run(main())

