sum=0
t=1
n=int(input("Enter the Number of terms:"))
x=int(input("Enter the Value of'x'"))
for i in range(1,n+1):
    num=(x**i)
    den=i*2-1
    sum+=t*(num/den)
    t*=-1
    print(num,den)
print("The Sum is",sum)
