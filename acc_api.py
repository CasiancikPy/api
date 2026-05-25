import requests
import os

from dotenv import load_dotenv
from urllib.parse import urlparse

BASE_URL = 'https://clc.li/api'


def shorten_link(api_token, url):
    layout = {
        'url': url
    }

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{BASE_URL}/url/add",
        headers=headers,
        json=layout
    )
    response.raise_for_status()
    return response.json()


def count_clicks(api_token):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    params = {
        'limit': '2',
        'page': '1',
        'short': '--'
    }

    response = requests.get(
        f"{BASE_URL}/urls",
        headers=headers,
        params=params)
    
    response.raise_for_status()

    result = response.json()

    if result['error'] == 1:
        print('Error')
        return None

    return result['data']['clicks']


def is_bitlink(link):
    url = urlparse(link)
    if url.netloc == 'clc.li':
        return True
    else:
        return False


def main():
    load_dotenv()
    API = os.getenv('API_TOKEN')
    url = input('URL:')

    parsed_result = is_bitlink(url)
    if parsed_result is True:
        print('Это короткая ссылка')
        try:
            data = count_clicks(API)
            print(data)
        except requests.exceptions.HTTPError as error:
            print('HTTPError', error.status_code)
    else:
        print('Это не короткая ссылка')
        try:
            short_link = shorten_link(API, url)
            print('Короткая ссылка:', short_link['shorturl'])
            link = short_link['shorturl']
            if 'error' in short_link:
                print('Error:', short_link['error'])
            else:
                print('Короткая ссылка:', short_link['shorturl'])
        except requests.exceptions.HTTPError as error:
            print('HTTPError', error.status_code)


if __name__ == '__main__':
    main()