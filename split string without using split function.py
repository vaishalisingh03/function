import string


def split():
    word="my name is vaishali singh"
    list=[]
    str=""
    for i in word:
        if i==" ":
            list.append(str)
            str=""
        else:
            str+=i
    if str:
        list.append(str)
    print(list)
split()