import os
from multiprocessing import Pool

import variables
from data_cleaner import cleanData
from downloader import download
from pklutils import loadWordList


def savePage(key, value, content):
    head = "https://www.collinsdictionary.com/dictionary/english/"
    item = value.replace(head, '')
    if item in ['con', 'nul']:
        item += '_1'
    output_file = content['dir'] + '/' + item + '.html'
    if not os.path.exists(output_file):
        page = download(item, None, value)
        html = cleanData(page, content)
        if html is not None:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(key + '\n' + html)


def crawl(content):
    word_list = loadWordList(content['list_file'])
    print("-------------- START CRAWLING --------------")
    pool = Pool(12)
    for key, value in word_list.items():
        pool.apply_async(savePage, args=(key, value, content))
    print('------------------ WAITING ------------------')
    pool.close()
    pool.join()
    print('----------------- ALL DONE ------------------')


if __name__ == "__main__":
    crawl(variables.word)
