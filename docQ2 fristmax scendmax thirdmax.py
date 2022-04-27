def max():
    a=[6,9,8,2,21]
    max1=0
    max2=0
    max3=0
    i=0
    while i<len(a):
        j=0
        while j<len(a):
            if a[j]>max1:
                max1=a[j]
            elif a[j]>max2 and a[j]!=max1:
                max2=a[j]
            elif a[j]>max3 and a[j]!=max2 and a[j]!=max1:
                max3=a[j]
            j+=1
        i+=1
    print(max1)
    print(max2)
    print(max3)
max()