# coding: utf-8

import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


def download(item, head):
    url = head + item
    # Avoid HTTP 403 Forbidden: 避免发生403错误
    header = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.93 Safari/537.36'
    }
    try:
        print("Getting url:" + url)
        response = requests.get(url, headers=header)
        response.raise_for_status()
    except HTTPError as err:
        print("There is an HTTP error in your network:\n" + err)
    except Exception as e:
        print(e)
    else:
        return BeautifulSoup(response.content, 'lxml', from_encoding='utf-8')
