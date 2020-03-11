import os
from multiprocessing import Pool

import variables
import logging
from data_cleaner import cleanData
from downloader import download
from pklutils import loadWordList

file_hanlder = logging.FileHandler(filename='err.log', encoding='utf-8')
logging.basicConfig(handlers=[file_hanlder], level=logging.WARNING)


def savePage(key, value, content):
    head = "https://www.collinsdictionary.com/dictionary/english/"
    item = value.replace(head, '')
    if item in ['con', 'nul']:
        item += '_1'
    output_file = content['dir'] + '/' + item + '.html'
    if not os.path.exists(output_file):
        page = download(item, None, value)
        if page is None or page.find("span", class_="cf-error-code"):
            logging.error(f"Failed to get entry: {key}")
        else:
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
    pool.close()
    pool.join()
    print('----------------- ALL DONE ------------------')


if __name__ == "__main__":
    crawl(variables.word)
