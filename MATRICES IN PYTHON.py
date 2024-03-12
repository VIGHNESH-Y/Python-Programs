n=int(input("Enter the Size of Square Matrix:"))
A=[]
for i in range(n):
    t=[]
    for i in range(n):
        x=int(input("Enter the Elements:"))
        t.append(x)
    A.append(t)
print("Square Matrix Form")
for i in range(n):
    for j in range(n):
        print(A[i][j],'  ',end='')
    print()
print("The Output Value")
'''for j in range(n):
    for i in range(n):
        if j>=n-i-1:
            print(A[i][j],'  ',end='')
        else :
            print("   ",end='')
    print()'''
'''for i in range(n):
     for j in range(n):
         if i>=j:
             print(A[i][j],'  ',end='')
     print()'''
'''for i in range(n):
    for j in range(n):
        if i+j<=n-1:
               print(A[i][j],'  ',end='')
    print()'''
'''for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print(A[i][j],'  ',end='')
    print()'''
            
            
        
