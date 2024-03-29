# coding: utf-8

import socket

import requests
import socks
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError


def download(item: str, head: str, url: str = None) -> BeautifulSoup:
    if head is not None:
        url = head + item
    # Avoid HTTP 403 Forbidden: 避免发生403错误
    header = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.93 Safari/537.36'
    }
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket
    try:
        response = requests.get(url, headers=header, timeout=10)
        response.raise_for_status()
    except HTTPError:
        pass
    except Exception as e:
        print(e)
    else:
        return BeautifulSoup(response.content, 'lxml', from_encoding='utf-8')
