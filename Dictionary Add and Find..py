ch="yes"
while ch=='yes':
    print("\t\t\t\t\t\t\t\t\t\tCUSTOMER DETAILS")
    print("\t\t\t\t\t\t\t\t\t\t***************")
    n=int(input("How many Customers Want to be registered:"))
    dic1={}
    for i in range(1,n+1):
        dic2={}
        num=int(input("Enter the Consumer Telephone Number:"))
        name=input("Enter the Consumemer's name:")
        address=input("Enter the Adress of the Consumer:")
        dic2["Address"]=address
        dic2["Name"]=name
        dic1[num]=dic2
    same_dict="yes"
    while same_dict=="yes":
        print("Enter '1' to Find the Telephone Number from the Dictionary\nEnter '2' to Sort the User Info")
        choice=int(input("Enter your Choice:"))
        if choice== 1:
            find=int(input("Enter the Number to be found from the Database:"))
            for i in dic1:
                if i==find:
                    print()
                    print("Searching....")
                    print()
                    print("The number",i,"is found in the Database!!")
                    print()
                    print("Name of the User:",dic1[find]["Name"],"\n\nAddress of the user",dic1[find]["Address"])
                    break
                    print()
                else:
                    print()
                    print("Error 404")
                    print()
                    print("Suggested Number is not registered with the company")
        elif choice==2:
            dict3=list(dic1.items())
            for i in range(n):
                for j in range(n-1-i):
                    if dict3[j][0]>dict3[j+1][0]:
                        dict3[j],dict3[j+1]=dict3[j+1],dict3[j]
                
            d = dict(dict3)
            print()
            for i in d:
                print(i,d[i]['Name'],d[i]['Address'])
        else:
            Print("It is a Invalid Choice")
        same_dict=input("Do you want to continue with the same dictionary('yes'(or)'no'):")
    ch=input("Do you want to input a new dictionary('yes'(or)'no')")
                 
            

           
