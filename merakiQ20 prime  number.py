def prime(a):
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count+=1
        i+=1
    if count==2:
        print("prime num",a)
    else:
        print("not prime",a)
b=int(input('enter number'))
prime(b)
