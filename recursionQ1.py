def fac(a):
    if a==1:
        return 1
    else:
        return(a*fac(a-1))
a=4
c=fac(a)
print(c)
