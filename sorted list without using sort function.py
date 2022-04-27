def sort():
    list=[8,7,4,2,9,6,3,1,5]
    i=0
    while i<len(list):
        j=0
        while j<len(list):
            if list[i]<list[j]:
                c=list[i]
                list[i]=list[j]
                list[j]=c
            j+=1
        i+=1
    print(list)
sort()