def num():
    a=[1450,960000,1050,50]
    i=0
    b=[]
    while i<len(a):
        while a[i]%10 == 0:
            a[i]//=10
        else:
            b.append(a[i])
        i+=1
    print(b)
num()



