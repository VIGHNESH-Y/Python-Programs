lower= int(input("Enter a Lower Limit:: "))
upper=int(input("Enter the Upper Limit:"))
print("The Prime Numbers between",lower,"AND",upper,"Are",end=" ")
for i in range(lower,upper+1):
    if(i>1):
        for j in range(2,i):
            if(j%i)==0:
                break
            else:
                print(j,"Is a prime number")


