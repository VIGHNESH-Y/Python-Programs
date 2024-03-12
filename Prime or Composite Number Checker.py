check="yes"
while check=="yes":
        lower=int(input("Enter the lower limit::"))
        upper=int(input("Enter the upper limit::"))
        
        for i in range(lower,upper):
            if i>1:
                for j in range(2,i):
                    if(i%j)==0:
                       print(i,"is a composite number")
                       break
                else:
                    print(i,"Is a prime numer")
        check=input("Do you want to contiue?:Yes/no::")

        
