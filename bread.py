a=int(input("enter no. of loaves:"))
b=int(input("enter no. of old loaves:"))
c=185
d=a*185
e=b*60*185/100
if(a<0 or b<0):
    print("error")
else:
    print("regular price",c)
    print("the price of new loaves",d)
    print("old loaves",e)
    print("total amount",d+e)
