def febonic(n):
    if n==1:
        return 0
    elif n==2                 :
        return 1
    else:
        return febonic(n-1)+febonic(n-2)
n=4
i=1
while i<=n:
    print(febonic(i))
    i+=1



