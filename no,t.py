a=int(input("enter number"))
i=1
while i<=a:
    b=1
    while b<=a-i:
        print(" ",end=" ")
        b=b+1
    c=1
    while c<=i:
        print("*",end=" ")  
        c=c+1
    print()
    i=i+1      


