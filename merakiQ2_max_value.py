def my_function():
    a=[3,8,99,45,7]
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i+=1
    print(max)
my_function() 
