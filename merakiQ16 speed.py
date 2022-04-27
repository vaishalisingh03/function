def speed(a):
    if a<=70:
        print("70")
    elif a>70:
        n=(a-70)//5
        if n<12:
            print(n)
        else:
            print("license suspend",n)
speed(85)
speed(135)