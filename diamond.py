#Diamond printing with using "*" symbol
a=int(input("Enter the no of rows."))
b=a-1
for i in range(1,a):
    for j in range(1,b):
        print(" ",end=" ")
    for k in range(0,2*i-1):
        print("*",end=" ")
    print()
    b=b-1
c=a-2
d=1
for n in range(c,0,-1):
    for m in range(0,d):
        print(" ",end=" ")
    for l in range(2*n-1,0,-1):
        print("*",end=" ")
    print()
    d=d+1