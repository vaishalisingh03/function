def add():
    a=[[1,2,3],[2,4,5]]
    i=0
    while i<len(a):
        j=0
        while j<len(a[i]):
            x=i+1
            while x<len(a):
                y=0
                sum=0
                while y<len(a[x]):
                    if y==j:
                        sum=a[i][j]+a[x][y]
                        print(sum)
                    y+=1
                x+=1
            j+=1
        i+=1
add()




        

