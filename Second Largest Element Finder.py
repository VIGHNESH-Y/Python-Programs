n=int(input("Enter the Number of Elements to be Added into the List:"))
l=[]
for i in range(n):
    i=int(input("Enter the Values to Be Appended:"))
    l.append(i)
for i in range(n-1):
    for j in range(n-i-1):
        if(l[j] > l[j+1]):
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp
            for i  in range(1,len(l)):
                key=l[i]
                j=i-1
                while j>=0 and key> l[j]:
                    l[j+1]=l[j]
                    j-=1
                    l[j+1]=key
print("The Original List is",l)
r=set(l)
print(r)
t=list(r)
m=(t[-2])
print("The Second Largest Element in the List is",m)





