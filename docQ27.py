def tab():
    a=int(input("enter number"))
    b=int(input("enter number"))
    while a<=b:
        i=1
        while i<=10:
            print(a,"*",i,"=",a*i)
            i+=1
        print()
        a+=1
tab()