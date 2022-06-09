a=int(input("enter number"))
r=1
while r<=a:
    b=1
    while b<=a-r:
        print(" ",end="")
        b=b+1
    c=1
    while c<=r:
        print(c,end="")
        c=c+1
    print()
    r=r+1
