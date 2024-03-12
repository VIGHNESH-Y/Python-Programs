ch="yes"
while ch== "yes":
    n=int(input("enter no of elements in tuple a -"))
    m=int(input("enter no of elements in tuple b -"))
    a1=()
    a2=()
    print()
    for i in range(n):
        a=(int(input("enter elements of tuple a- ")))
        a1+=(a,)
    print()
    for j in range(m):
        b=(int(input("enter elements of tuple b - ")))
        a2+=(b,)
    print()
    c=()
    i,j=n-1,m-1
    while i>=0 and j>=0:
        if a1[i]< a2[j]:
            c+=(a1[i],)
            i-=1
        else:
            c+=(a2[j],)
            j-=1
    while i>=0:
        c+=(a1[i],)
        i-=1
    while j>=0:
        c+=(a2[j],)
        j-=1
    print("tuple a- ",a1)
    print("tuple b- ",a2)
    print("merged tuple - ",c)
    
    ch=input("Do you want to continue (yes/no)- ")
    print()
