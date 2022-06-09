a=int(input("enter number"))
i=1
while i<=a:
    b=a
    while b>=i:
        print(" ",end="")
        b=b-1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+2
i=2
while i<=a:
    b=1
    while b<=i:
        print(" ",end="")
        b=b+1
    j=a
    while j>i:
        print("*",end="")
        j=j+1
    print()
    i=i+2                    

