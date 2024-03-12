choice="yes"
while choice=="yes":
    print("\t\t\t\t\tMenu Driven Program")
    print("\t\t\t\t\t********************")
    Final=[]
    Temporary=[]
    g=0
    a=0
    no=0
    t=0
    r=int(input('What is the len of the Tuple?:'))
    n=int(input("How many Values must each Tuple consist?:"))
    for i in range(r):
        for j in range(0,n):
            Temporary.append(int(input("Enter the Values to be Added:")))
        Final.append(Temporary)
        Temporary=[]  
    c=tuple(Final)
    print("The Original Tuple is:",c)
    for j in c:
        for s in j:
            t=t+s
            avg=t/len(j)
        print("The  Average of Split Tuples",j,"is:",avg)
        a+=t
        t=0
        tot_avg=a/(n*r)
    print("The Average Value of the Tuple is:",tot_avg)
    choice=input("Do you want to continue the Program?(yes or no::)")
    
    


    
        
