# coding: utf-8

from os import path

from downloader import download
from pklutils import dumpWordList, loadWordList
import variables


def getList(content):
    char_list = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    if path.exists(content['list_file']):
        dicts = loadWordList(content['list_file'])
    else:
        dicts = {}
    if content == variables.word:
        getSubList(content['browse_url'] + "words-starting-with-digit", dicts, head=content['browse_url'])
    for char in char_list:
        page = download(content['list_head'] + char, head=content['browse_url'])
        browse_list = page.find('ul', class_='browse-list')
        links = browse_list.find_all('a')
        for link in links:
            getSubList(link['href'], dicts, head=content['browse_url'])
        dumpWordList(dicts)


def getSubList(url, dicts, head):
    page = download(url, head='')
    browse_list = page.find('ul', class_='browse-list')
    links = browse_list.find_all('a')
    for link in links:
        dicts.update({link.text: link['href']})


if __name__ == "__main__":
    getList(variables.word)
