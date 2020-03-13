# coding: utf-8
import os

all_files = os.listdir('thes')
keys = ['thes/' + key for key in all_files]
fout = open("thes.txt", "w", encoding="utf-8")

for key in keys:
    fin = open(key, "r", encoding="utf-8")
    for line in fin.readlines():
        fout.write(line)
    fout.write("\n</>\n")
    fin.close()

fout.close()
