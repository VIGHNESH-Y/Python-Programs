ch="yes"
while ch=="yes":
    print("\t\t\t\t\t\t Sorting In List")
    print("\t\t\t\t\t\t******************")
    a = []
    number = int(input("Please Enter the Total Number of Elements::"))
    for i in range(number):
        value = int(input("Please enter the %d Element of List1 : " %i))
        a.append(value)
    choice=int(input("1. Sort in ascending order using Bubble sort, 2. Sort in Descending order using Insertion sort::"))
    if choice==1:
            print("The List Before Sorting:",a)
            n=len(a)
            for i in range(n):
                for j in range(0,n-1,1):
                    if a[j]>a[j+1]:
                        a[j],a[j+1]=a[j+1],a[j]
            print("The List After Sorting:",a)
    if choice==2:
        print("The Original List is:",a)
        for i in range(1,len(a)):
            key=a[i]
            j=i-1
            while j>=0 and key<a[j]:
                a[j+1]=a[j]
                j=j-1
            else:
                a[j+1]=key
        print("The Sorted List Using Insertion Sort is:",a[::-1])
    ch=input("Do you want to Continue(yes or no)::")





