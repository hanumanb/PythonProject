"""HTTP client pattern with timeout and status validation.

Install requests with: pip install requests
This example targets a public test endpoint. It may require internet access.
"""
import requests

def fetch_post(post_id: int) -> dict:
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        timeout=(3.05, 10),
    )
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    try:
        print(fetch_post(1))
    except requests.RequestException as exc:
        print(f"API request failed: {exc}")
