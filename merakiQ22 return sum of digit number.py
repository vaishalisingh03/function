def sum(num):
    sum=0
    modulus=0
    while num!=0:
        modulus=num%10
        sum+=modulus
        num//=10
    return sum
print(sum(123))