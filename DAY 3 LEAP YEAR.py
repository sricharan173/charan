n=int(input("enter year:"))
if(n>0):
    if(n%4==0 or n%400==0):
        print("given year is leap year")
    else:
        print("given year is not leap year")
        if(n%4!=0):
            n-=int(n%4)
            print("leap year is:",n)
else:
    print("invalid")
