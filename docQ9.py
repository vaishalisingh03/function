def square():
    i=1
    x=[]
    y=[]
    while i<=5:
        x.append(i*i)
        i+=1
    j=26
    k=[]
    while j<=30:
        k.append(j*j)
        j+=1
    y.append(x)
    y.append(k)
    print(y)
square()
