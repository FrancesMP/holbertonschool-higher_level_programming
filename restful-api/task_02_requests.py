import requests
import csv


def fetch_and_print_posts():

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save them to a CSV file."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()

        # Clean and structure the data
        structured_data = []
        for post in posts:
            post_dict = {
                'id': post['id'],
                'title': post['title'].replace('"', '""')
                .replace('\n', ' ').strip(),
                'body': post['body'].replace('"', '""')
                .replace('\n', ' ').strip()
            }
            structured_data.append(post_dict)

        # Write to CSV with proper formatting
        with open("posts.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"],
                quoting=csv.QUOTE_NONNUMERIC,
                delimiter=','
            )
            writer.writeheader()
            writer.writerows(structured_data)
