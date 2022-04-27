def speed(a):
    if a<=70:
        print("ok")
    elif a>70:
        n=(a-70//5)
        if n<12:
            print(n)
        else:
            print("licence suspend",n)
speed(45)
speed(120)