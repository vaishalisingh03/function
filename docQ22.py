def num():
    a=int(input("enter number"))
    if a%3==0 and a%5==0:
        print("fizz","buzz")
    elif a%5==0:
        print("buzz")
    elif a%3==0:
        print("fizz")
    else:
        print("same number")
num()