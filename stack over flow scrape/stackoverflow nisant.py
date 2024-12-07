import requests
import json
from datetime import datetime
import time

def fetch_stackoverflow_questions(tag=None, page=1, pagesize=100):
    """
    Fetch recent questions from Stack Overflow using the Stack Exchange API.

    :param tag: Optional; tag to filter questions by.
    :param page: Page number to fetch.
    :param pagesize: Number of questions per page.
    :return: List of questions.
    """
    base_url = "https://api.stackexchange.com/2.3/questions"
    params = {
        'order': 'desc',
        'sort': 'creation',
        'site': 'stackoverflow',
        'page': page,
        'pagesize': pagesize
    }

    if tag:
        params['tagged'] = tag

    response = requests.get(base_url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code, response.json()}")

    data = response.json()
    return data['items']

def save_questions_to_json(questions, filename):
    """
    Save the list of questions to a JSON file.

    :param questions: List of questions to save.
    :param filename: Name of the JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(questions, json_file, indent=4)
    print(f"Questions have been saved to {filename}")

if __name__ == "__main__":
    # tag = input("Enter a tag to filter questions by (or leave blank for all questions): ").strip()
    # page = int(input("Enter the page number to fetch: "))
    # pagesize = int(input("Enter the number of questions per page: "))

    try:
        for i in range(10001, 2000000, 5):
            questions = fetch_stackoverflow_questions(page=i)
            # Generate a filename with the current date and time
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"stackoverflow_questions_{timestamp}.json"
            save_questions_to_json(questions, filename)

            print(f"Fetched and saved page {i} to {filename}")
            time.sleep(4)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
