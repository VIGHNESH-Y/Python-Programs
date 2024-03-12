row=int(input("Enter the Row Size:"))
col=int(input("Enter the ColSize:"))
A=[]
for i in range(row):
    t=[]
    for i in range(col):
        x=int(input("Enter the Elements:"))
        t.append(x)
    A.append(t)
print("In Matrix form:")
for i in range(col):
    s=0
    for j in range(row):
        s=A[j][i]
print("The sum of column",i+1,"is:",s)
