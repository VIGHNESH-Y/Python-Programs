str=input("Enter the String to be checked:")
b = ""
for i in range(len(str)):
    if (i%2)==0:
        b+=str[i]
print(b.upper())
 
