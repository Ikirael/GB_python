
from itertools import groupby, starmap
from os import path

def rle_encode(text = "text_words.txt", code_text = "text_code_words.txt"):
    if path.exists(text) and not path.exists(code_text):
        with open(text) as f1, open(code_text,'a') as f2:
            for i in f1:
                for ch, v in groupby(i):
                    f2.write("".join(f"{len(list(v))} {ch}"))
    else: 
        ("Error")

def rle_decode(name):
    if path.exists(name):
        with open(name) as f1:
            n = ""
            for k in f1:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_nums.append([int(n), i])
                        n = ""
                    print("".join(starmap(lambda x, y: x * y, word_nums)))
    else:
        print("Error")

rle_encode(input("Enter file name:"), input("Enter file name to record:"))
rle_decode(input("Enter encode file name: "))