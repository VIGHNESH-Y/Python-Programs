choice="yes"
while choice=="yes":
    print("\t\t\t\t\tMENU DRIVEN PROGRAM-LIST")
    print("\t\t\t\t\t************************")
    n=int(input("Enter no. of terms : "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter an element of the list : ")))
    print("The original list is",l)
    choice2="yes"
    while choice2=="yes":
        print("1.Find the largest element\n2.Find the second largest element\n3.Print the palindrome numbers in the list")
        ch=int(input("Enter your choice : "))
        if ch==1:
            lar=l[0]
            for j in l:
                if lar<j:
                    lar=j
            print("The largest no. present in",l,"is",lar)
      
            x=[]
            for i in l:
                j=i
                rev=0
                while j>0:
                    rev=rev*10+j%10
                    j//=10
                if i==rev and i not in x:
                    x+=[i]
            if x:
                print("The palindrome numbers are",end=" ")
                for a in x:
                    print(a,end=" ")
            else:
                print("There are no palindromes in the list",l)
        print()       
        choice2=input("Do you want to continue with the same list?(yes/no)\n")
        print()
    choice=input("Do you want to continue with a new list?(yes/no)\n")
else:
    print()
    print("End of program.")
   
 

