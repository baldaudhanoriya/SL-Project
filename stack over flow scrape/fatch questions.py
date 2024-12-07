import requests
import json

def fetch_stackoverflow_questions(tag=None, page=1, pagesize=10):
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
        raise Exception(f"Error fetching data: {response.status_code}")

    data = response.json()
    return data['items']

def print_questions(questions):
    """
    Print details of the fetched questions.

    :param questions: List of questions to print.
    """
    for question in questions:
        title = question['title']
        creation_date = question['creation_date']
        link = question['link']
        print(f"Title: {title}")
        print(f"Creation Date: {creation_date}")
        print(f"Link: {link}")
        print(que)
        print("="*50)

if __name__ == "__main__":
    tag = input("Enter a tag to filter questions by (or leave blank for all questions): ").strip()
    page = int(input("Enter the page number to fetch: "))
    pagesize = int(input("Enter the number of questions per page: "))

    try:
        questions = fetch_stackoverflow_questions(tag, page, pagesize)
        print_questions(questions)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
