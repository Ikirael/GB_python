
def CreateVoc(lst:list):
    voc = {}
    for i in range(len(lst)):
        if lst[i][0] in voc:
            voc[lst[i][0]].append(lst[i])
        else:
            lst2 = []
            lst2.append(lst[i])
            voc[lst[i][0]] = lst2
            
    return voc

# return {lst[i][0]:lst[i] for i in range(len(lst))}

lst = (input("Введите список имен в кавычках через запятую: ").replace('"', '')).split(", ")
print(lst)
voc = CreateVoc(lst)
print(voc)