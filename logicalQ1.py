def sum():
    a=[[1,2,3],[3,6,4]]
    i=0
    while i<len(a):
        j=0
        while j<len(a[i]):
            x=i+1
            while x<len(a):
                y=0
                sum=0
                while y<len(a[x]):
                    if j==y:
                        sum=a[i][j]+a[x][y]
                        print(sum)
                    y=y+1
                x=x+1
            j=j+1
        i=i+1
sum()



    
