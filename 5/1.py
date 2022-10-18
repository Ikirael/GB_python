# 38. Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

from random import sample

def list_rand_words(count: int, alp: str = "абв"):
    words_list = []
    for i in range(count):
        letters = sample(alp,3)
        words_list.append("".join(letters))
    return " ".join(words_list)

def simple_sentence(words:str) -> str:
    return " ".join(i for i in words.split() if i!="абв")

lst = list_rand_words(int(input("Number of words: ")))
print(lst) 
lst_new = simple_sentence(lst)
print(lst_new)