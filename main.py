import os
from multiprocessing import cpu_count, Pool

import variables
import logging
from data_cleaner import cleanData
from downloader import download
from pklutils import loadWordList

file_handler = logging.FileHandler(filename='err.log', encoding='utf-8')
logging.basicConfig(handlers=[file_handler], level=logging.WARNING)


def savePage(key, value, content):
    if not os.path.isdir(content['dir']):
        os.mkdir(content['dir'])
    head = content['head']
    item = value.replace(head, '')
    if item in ['con', 'aux', 'prn']:
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
    # with open("cet-wordlist.txt", "r", encoding="utf-8") as f:
    #     urls = f.readlines()
    # word_list = {
    #     line.strip().replace(content['head'], ''): line.strip()
    #     for line in urls
    # }
    print("-------------- START CRAWLING --------------")
    pool = Pool(cpu_count())
    for key, value in word_list.items():
        pool.apply_async(savePage, args=(key, value, content))
    pool.close()
    pool.join()
    print('----------------- ALL DONE ------------------')


if __name__ == "__main__":
    crawl(variables.word)
    # savePage("put up the shutters", "https://www.collinsdictionary.com/dictionary/english/put-up-the-shutters", variables.word)
