import requests


def fetch_data():
    # get test
    response = requests.get("https://api.github.com")
    print(f"Status Code: {response.status_code}")
    print(f"Server: {response.headers.get('Server')}")


if __name__ == "__main__":
    fetch_data()
