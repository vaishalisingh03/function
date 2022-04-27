def name():
    list=["aba","xyi","aba","sys","232"]
    i=0
    c=0
    while i<len(list):
        if list[i][0]==list[i][-1]:
            c+=1
        i+=1
    print(c)
name()
 