def num():
    a=[3,78,8,9,1]
    i=0
    mini=a[0]
    while i<len(a):
        if a[i]<mini:
            mini=a[i]
        i+=1
    print(mini)   
num()