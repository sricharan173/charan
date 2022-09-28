p=int(input("enter the pinciple amount:"))
t=int(input("enter no. of years:"))
choice=str(input("is customer is senior citizen(YC/NC):"))
if choice in('NC','YC'):
    if choice =='NC':
        r=10
    else:
        r=12
si=p*t*r/100
if(p<0 or t<0):
    print("invalid")
else:
    print("simple interest is:",si)
