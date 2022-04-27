def num():
    a=[2,-7,5,-64,-14]
    count1=0
    count2=0
    i=0
    while i<len(a):
        if a[i]<0:
            count1+=1
        else:
            count2+=1
        i+=1
    print("negative",count1)
    print("positive",count2)
num()
