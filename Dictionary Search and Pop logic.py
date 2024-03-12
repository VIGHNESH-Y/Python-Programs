cont = "y"
while cont == 'y':
    print("\t\t\tCUSTOMER DETAILS")
    print("\t\t\t****************")
    n = int(input("No. of customers : "))
    d = {}
    for i in range(n):
            tele = int(input("Enter a customer's telephone number : "))
            d[tele] = dict(name = input("Enter the customer's name : "),address = input("Enter the customer's address : "))
    cont2 = 'y'
    while cont2 == 'y':
        print('1 - Search for a customer for given telephone number\n2 - Sorting the dictionary of phone numbers in ascending order')
        ch = int(input("Enter your choice : "))
        if ch == 1:
            tph = int(input("Enter the customer's telephone number : "))
            for i in d:
                if tph == i:
                    print(i,"found","\nName:",d[i]['name'],"\nAddress:",d[i]['address'])
                    break
            else:
                print("A customer with telephone number",tph,"is not found")
        elif ch ==2 :
            l = list(d.keys())
            for i in range(len(l)-1):
                for j in range(len(l)-1-i):
                    if l[j]>l[j+1] :
                        l[j+1],l[j] = l[j],l[j+1]
            d2={}
            for k in l:
                d2[k] = d[k]
            d = dict(d2)
            for i in d:
                print(i,d[i]['name'],d[i]['address'])

        else :
            print("Invalid choice")
        cont2 = input("Do you want to continue with the same dictionary of customers?(y/n) :")
       
    cont = input("Do you want to continue with the program?(y/n) :")
