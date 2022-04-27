def name():
    a="vaishali"
    i=0
    count=0
    while i<len(a):
        if a[i]=="a":
            count+=1
        i+=1
    if count==2:
        print("yes")
    else:
        print("no")
name()