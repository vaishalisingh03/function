def perfect_num():
    a=int(input("enter number"))
    i=1
    while i<a:
        j=1
        sum=0
        while j<=i:
            if a%j==0:
                sum+=j
            j+=1
        i+=1
    if sum==a:
        print("perfect numbber",a)
    else:
        print("not perfect",a)
perfect_num()