n=int(input("Enter no. of terms : "))
l=[]
for i in range(n):
    ch=1
    if ch==1:
        l.append(int(input("Enter an element of the list : ")))
        print("User Input List:",l)
        ch=int(input("Enter 1 to Proceed:"))
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
                        
print(l)

