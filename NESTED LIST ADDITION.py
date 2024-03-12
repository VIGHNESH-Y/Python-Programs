n=int(input("Enter the len of the Overall List:"))
t=[]
for i in range(n):
    e=int(input("Enter the Length of each nested List:"))
    for j in range(e):
        l=[]
        n=int(input("Enter the Values to be Added in Each List:"))
        l.append(n)
    t.append(n)
print(t)
