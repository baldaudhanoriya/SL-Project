import requests
import json
import time

# GitHub API URL
GITHUB_API_URL = "https://api.github.com"

# Open file that has token information
with open("github_token.txt", "r") as file:
    token = file.read().strip()

# Replace with your GitHub personal access token
ACCESS_TOKEN = token

# Authentication headers
headers = {
    "Authorization": f"token {ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_repositories_by_date(start_date, end_date, per_page=100, pages=10):
    """Fetch repositories based on their creation date."""
    query = f"created:{start_date}..{end_date}"
    repositories = []
    for page in range(1, pages + 1):

        print(f"getting repositories of date: {start_date}, page: {page}")

        url = f"{GITHUB_API_URL}/search/repositories?q={query}&per_page={per_page}&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            repositories.extend(data['items'])
            # Save fetched data incrementally
            with open("repositories.json", "a") as file:
                json.dump(data['items'], file, indent=4)
        else:
            print(f"Failed to fetch repositories: {response.status_code, response.json()}")
            time.sleep(65)
        time.sleep(2)  # To avoid hitting rate limits
    return repositories

def get_languages(repo_url):
    """Fetch the languages used in a given GitHub repository."""
    response = requests.get(repo_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch languages for repository {repo_url}: {response.status_code}")
        return {}

def fetch_and_store_languages(repos):
    """Fetch languages for each repository and store the data in a JSON file."""
    languages_data = {}
    for repo in repos:
        repo_name = repo['full_name']
        languages_url = repo['languages_url']
        languages = get_languages(languages_url)
        languages_data[repo_name] = languages
        # Save fetched data incrementally
        with open("languages.json", "a") as file:
            json.dump({repo_name: languages}, file, indent=4)
        time.sleep(1)  # To avoid hitting rate limits
    return languages_data


from datetime import datetime, timedelta

def get_month_details(year_month):
    try:
        # Parse the input string into year and month
        year, month = map(int, year_month.split('-'))
        
        # First day of the month
        first_date = datetime(year, month, 1).strftime('%Y-%m-%d')
        
        # Calculate the last day of the month
        if month == 12:  # If December, next month is January of the next year
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)
        last_date = (next_month - timedelta(days=1)).strftime('%Y-%m-%d')
        
        # Calculate the previous month
        if month == 1:  # If January, previous month is December of the previous year
            prev_month_year = year - 1
            prev_month = 12
        else:
            prev_month_year = year
            prev_month = month - 1
        
        previous_month = f"{prev_month_year:04d}-{prev_month:02d}"
        
        return {
            "first_date": first_date,
            "last_date": last_date,
            "previous_month": previous_month
        }
    except ValueError:
        return "Invalid input! Please use the format 'yyyy-mm'."


from datetime import datetime, timedelta

def get_earlier_date(date_str, days):
    # Parse the input date string into a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Subtract the specified number of days
    earlier_date = date - timedelta(days=days)
    
    # Format the resulting date back into a string
    return earlier_date.strftime('%Y-%m-%d')



def main():
    end_date = "2014-06-25"
    gap = 4

    # Clear previous data from the files if needed
    with open("repositories.json", "w") as file:
        file.write("")  # Initialize as empty JSON array

    with open("languages.json", "w") as file:
        file.write("{}")  # Initialize as empty JSON object


    while(gap < 10):

        gap = 100//int(end_date.split("-")[0][2:])
        start_date = get_earlier_date(end_date, gap)
        
        repos = get_repositories_by_date(start_date, end_date)

        print(start_date, "done", f"gap:{gap}")
        end_date = get_earlier_date(start_date, 1)


    with open("repositories.json", "r") as file:
        repos = json.load(file)

    fetch_and_store_languages(repos)

if __name__ == "__main__":
    main()

print("done")
