n=int(input("Enter the number of elements to be added into the List:"))
s=[]
t=[]
for i in range(n):
    x=int(input("Enter the Intergers::"))
    s.append(x)
print("The original list is:",s)
for i in (s):
    if i%2==0:
        e=i*2
        t.append(e)

    else:
        f=i*3
        t.append(f)
print("The final list is",t)
