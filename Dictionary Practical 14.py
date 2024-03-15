n=int(input("How many Friends do you have:"))
fd={}
for i in range(n):
    print("Enter the Detail of Friend",i+1)
    name=input("Enter the Name:")
    ph=int(input("Enter the Phone Number::"))
    fd[name]=ph
    print("The Dictionary is:",fd)
ch=0
while ch!=7:
    print("\t\t\t\tMENU")
    print("1.Display the name of your Friends")
    print("2.Add a New Friend")
    print("3.Delete a Exisiting Friend")
    print("4.Modify the Phone Number")
    print("5.Search for a Friend")
    print("6.Sort the names")
    print("7.Exit")
    ch=int(input("Enter your Choice"))
    if ch==1:
        print(fd)
    elif ch==2:
        print("Enter Details of a New Friend:")
        name=input("Enter the name of the New Friend")
        ph=int(input("Enter the Phone Number of the New friend:"))
        fd[name]=ph
    elif ch==3:
        nm=input("Enter friend Name to be Deleted:")
        res=fd.pop(nm,-1)
        if res!=-1:
            print(res,"Deleted")
        else:
            print("There are no such friends:")
    elif ch==4:
        name=int("Enter your Friends name:")
        ph=int(input("Enter corrected Phone Number"))
        fd[name]=ph
    elif ch==5:
        name=input("Enter your Friend's Name:")
        if name in fd:
            print(name,"Exists in the Dictionary")
        else:
            print(name,"Does not exist in the dictionary")
    elif ch==6:
        lst=sorted(fd)
        print("{",end="")
        for a in lst:
            print(a,":",fd[a],end="")
        print("}")
    elif ch==7:
        break
    else:
        print("Please Enter a Valid Choice")
        
            
