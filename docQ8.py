def chr():
    a="The quick Brow Fox"
    uppercase=0
    lowercase=0
    i=0
    while i<len(a):
        if a[i]>="a" and a[i]<="z":
            lowercase+=1
        elif a[i]>="A" and a[i]<="Z":
            uppercase+=1
        i+=1
    print(uppercase)
    print(lowercase)
chr()
        