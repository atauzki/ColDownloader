import pickle

f = open("theslist.pkl", "rb")
word_list = pickle.load(f)
f.close()

fail_fp = open("err.log", "r", encoding="utf-8")
fail_list = [line.replace("\n", "") for line in fail_fp.readlines()]
fail_fp.close()

fail_dict = {key: word_list[key] for key in fail_list}
print(len(fail_dict))

with open("theslist.pkl", "wb") as f:
    pickle.dump(fail_dict, f)
