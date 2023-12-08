import requests
from bs4 import BeautifulSoup

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    source = requests.get("https://www.imdb.com/chart/top/", headers=headers)
    source.raise_for_status()   # to get error if url not right

    soup = BeautifulSoup(source.text, 'html.parser')
    print(soup)

except Exception as e:
    print(e)