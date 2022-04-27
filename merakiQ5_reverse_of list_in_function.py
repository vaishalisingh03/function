def reverse():
    a=[2,3,6,7]
    i=-1
    b=[]
    while i>=-len(a):
        b.append(a[i])
        i-=1
    print(b)
reverse()