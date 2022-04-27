def sum(a,b):
    i=0
    sum=0
    sum1=0
    while i<len(a):
        sum+=int(a[i])
        sum1+=int(b[i])
        x=str(sum)
        y=str(sum1)
        i+=1
    print(x)
    print(y)
a="5","4"
b="34","5"
sum(a,b)

