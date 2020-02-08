import os
from multiprocessing import Pool

import variables
from data_cleaner import cleanData
from downloader import download
from pklutils import loadWordList


def savePage(item, content):
    item = item.replace(' ', '-').replace('/', '-').replace('?', '').replace(':', '-')
    output_file = content['dir'] + '/' + item + '.html'
    if not os.path.exists(output_file):
        page = download(item, head=content['url'])
        html = cleanData(page, content)
        if html is not None:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)


def crawl(content):
    if not os.path.isdir(content['dir']):
        os.mkdir(content['dir'])
    word_list = loadWordList(content['list_file'])
    print("-------------- START CRAWLING --------------")
    pool = Pool(12)
    for item in word_list:
        pool.apply_async(savePage, args=(item, content))
    print('------------------ WAITING ------------------')
    pool.close()
    pool.join()
    print('----------------- ALL DONE ------------------')


if __name__ == "__main__":
    crawl(variables.thes)
