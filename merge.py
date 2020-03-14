# coding: utf-8
import os
import re

from bs4 import BeautifulSoup
from mdict_utils.base.readmdict import MDX
from unidecode import unidecode


def merge_file(content):
    all_files = os.listdir(content['dir'])
    keys = [content['dir'] + "/" + key for key in all_files]
    fout = open(content["dir"] + ".txt", "w", encoding="utf-8")

    for key in keys:
        fin = open(key, "r", encoding="utf-8")
        for line in fin.readlines():
            fout.write(line)
        fout.write("\n</>\n")
        fin.close()

    fout.close()


def extract():
    mdx_keys = MDX("cet.mdx").keys()
    keys = [key.decode("utf-8") for key in mdx_keys]
    fout = open("derived.txt", "w", encoding="utf-8")
    for key in keys:
        decoded_key = unidecode(key)
        if decoded_key not in keys:
            fout.write(f"{decoded_key}\n@@@LINK={key}\n</>\n")
    fout.close()


def clean():
    fin = open("word.txt", "r", encoding="utf-8")
    fout = open("word-clean.txt", "w", encoding="utf-8")
    for line in fin.readlines():
        if re.match("^<link rel", line) is not None:
            soup = BeautifulSoup(line, "lxml")
            fout.write(str(soup))
        else:
            fout.write(line)
    fin.close()
    fout.close()


def get_wordlist_name():
    wldict = dict()
    fin = open("cet-wl.txt", "r", encoding="utf-8")
    for line in fin.readlines():
        if re.match("^\\w", line):
            value = line.strip()
        if re.match("^<link rel", line):
            soup = BeautifulSoup(line, 'lxml')
            key = soup.find("h2",
                            class_="wl").find("span",
                                              class_="orth").text.strip()
            wldict.update({key: value})
    fin.close()
    return wldict


def wordlist_fix(wldict):
    fin = open("cet.txt", "r", encoding="utf-8")
    fout = open("cet-fix.txt", "w", encoding="utf-8")
    for line in fin.readlines():
        if re.search("see also subject word lists", line) is not None:
            for key, value in wldict.items():
                old = "entry://" + key
                new = "entry://" + value
                line = re.sub(old, new, line)
            fout.write(line)
        else:
            fout.write(line)
    fin.close()
    fout.close()


def extend():
    fin = open("word.txt", "r", encoding="utf-8")
    fout = open("deriv.txt", "w", encoding="utf-8")
    for line in fin.readlines():
        if re.search(r"^\w", line):
            key = line.strip()
        if re.search("^<link", line):
            soup = BeautifulSoup(line, "lxml")
            # words1 = soup.select("div.mini_h2 span.orth")
            # words2 = soup.select("div.type-drv span.orth")
            words3 = soup.select("h2.h2_entry>span.orth")
            words = words3  # words1 + words2
            for word in words:
                word = word.text.strip()
                if not word.lower() == key.lower():
                    deriv_word = word
                    fout.write(f"{deriv_word}\n@@@LINK={key}\n</>\n")
    fin.close()
    fout.close()


if __name__ == "__main__":
    # merge_file(variables.word)
    # wldict = get_wordlist_name()
    # wordlist_fix(wldict)
    extend()
    # clean()
    # extract()
