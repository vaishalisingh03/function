def vote(age):
    if age>=18:
        print("able for voting")
    elif age<18:
        print("not able for voting")
age=int(input("enter number"))
vote(age)