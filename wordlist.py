# coding: utf-8

from os import path

from downloader import download
from pklutils import dumpWordList, loadWordList
from multiprocessing import Pool, Manager
import variables


def getList(content):
    char_list = [
        'digit', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    if path.exists(content['list_file']):
        dicts = loadWordList(content['list_file'])
    else:
        dicts = {}
    with Manager() as manager:
        if content == variables.word:
            getSubList(content['browse_url'] + "words-starting-with-digit", dicts, head=content['browse_url'])
        d = manager.dict(dicts)
        for char in char_list:
            if char in dicts:
                continue
            else:
                page = download(content['list_head'] + char, head=content['browse_url'])
                browse_list = page.find('ul', class_='bL')
                links = browse_list.find_all('a')
                pool = Pool(12)
                for link in links:
                    pool.apply_async(getSubList, args=(link['href'], d, content['browse_url']))
                pool.close()
                pool.join()
                # print(d)
                dumpWordList(dict(d), content['list_file'])


def getSubList(url, dicts, head):
    page = download(url, head='')
    browse_list = page.find('ul', class_='bL')
    links = browse_list.find_all('a')
    for link in links:
        dicts.update({link.text: link['href']})


if __name__ == "__main__":
    content = variables.word
    dicts = loadWordList(content['list_file'])
    print(len(dicts))
    print(dicts['evolution'])
    # getList(variables.word)
