def calkulater():
    a=int(input("enter the number:>"))
    b=int(input("enter the number:>"))
    op=str(input("enter the operetor:>"))
    if op=="+":
        print(a+b)
    elif op=="-":
        print(a-b)
    elif op=="*":
        print(a*b)
    elif op=="%":
       print(a%b)
    elif op=="/":
        print(a/b)
calkulater()
