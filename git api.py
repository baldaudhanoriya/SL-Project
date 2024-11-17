import requests
import json
import time

# GitHub API URL
GITHUB_API_URL = "https://api.github.com"


# open file that has token information:

with open("github token.txt", "r") as file:
    token = file.read().strip()

# Replace with your GitHub personal access token
ACCESS_TOKEN = token


input(ACCESS_TOKEN)

# Authentication headers
headers = {
    "Authorization": f"token {ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_repositories(query, per_page=100, pages=10):
    """Fetch repositories based on a search query."""
    repositories = []
    for page in range(1, pages + 1):
        url = f"{GITHUB_API_URL}/search/repositories?q={query}&per_page={per_page}&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            repositories.extend(data['items'])
        else:
            print(f"Failed to fetch repositories: {response.status_code}")
        time.sleep(1)  # To avoid hitting rate limits
    return repositories

def get_languages(repo_url):
    """Fetch the languages used in a given GitHub repository."""
    response = requests.get(repo_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch languages for repository {repo_url}: {response.status_code}")
        return {}

def fetch_and_store_repositories(query, filename="repositories.json"):
    """Fetch repositories and store their data in a JSON file."""
    repos = get_repositories(query)
    with open(filename, "w") as file:
        json.dump(repos, file, indent=4)
    print(f"Stored {len(repos)} repositories in {filename}")

def fetch_and_store_languages(repos, filename="languages.json"):
    """Fetch languages for each repository and store the data in a JSON file."""
    languages_data = {}
    for repo in repos:
        repo_name = repo['full_name']
        languages_url = repo['languages_url']
        languages = get_languages(languages_url)
        languages_data[repo_name] = languages
        time.sleep(1)  # To avoid hitting rate limits
    with open(filename, "w") as file:
        json.dump(languages_data, file, indent=4)
    print(f"Stored languages for {len(repos)} repositories in {filename}")

def main():
    query = "Machine Learning"  # Replace with your search query
    fetch_and_store_repositories(query)
    
    with open("repositories.json", "r") as file:
        repos = json.load(file)
    
    fetch_and_store_languages(repos)

if __name__ == "__main__":
    main()

print("done")