a=int(input("enter number"))
k=1
i=1
while i<=a:
    b=1
    while b<=a-i:
        print(" ",end=" ")
        b=b+1
    j=1
    while j<=k:
        print("*",end=" ")
        j=j+1
    k=k+2
    print()
    i=i+1        