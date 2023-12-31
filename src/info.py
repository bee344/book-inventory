import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")


def make_request(isbn):
    isbn_code = isbn + "+isbn"
    payload = {"q": isbn_code, "printType": "books", "key": API_KEY}
    url = "https://www.googleapis.com/books/v1/volumes"
    try:
        r = requests.get(url, params=payload, timeout=1, verify=True)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
    except requests.exceptions.ReadTimeout as errrt:
        print("Time out")
    except requests.exceptions.ConnectionError as conerr:
        print("Connection error")
