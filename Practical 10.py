ch="yes" 
while ch=="yes":
    print("\t\t\t\t\t\t\t\tNUMBER CONVERSIONS")
    print("\t\t\t\t\t\t\t\t******************")
    c=int(input("Enter 1 for Decimal to binary\nEnter 2 for Octal to decimal\nEnter 3 for Decimal to Hexadecimal::"))
    if c==1:
        n = int(input("Enter the Decimal Value to be converted:"))
        a=0
        bi=0
        c1=n
        while c1>0:                 
            r = c1%2
            bi=r*10**a + bi
            c1//=2
            a+=1
        print("The Binary Expansion of Decimal Value",n,"is",bi)
        ch=input("Do you want to re-start the conversion?(yes/no):")
    if c==2:
        n=int(input("Enter the Octal Value to be converted:"))
        n1=n
        dec=0
        e=0                             
        while n1>0:
            r=n1%10  
            dec=r*8**e+dec
            n1//=10
            e+=1
        print("The Decimal Expansion of Octal Value,",n,"is",dec)
        ch=input("Do you want to re-start the conversion?(yes/no):")
    if c==3:
        n=int(input("Enter decimal value:"))
        hexa=''
        n1=n
        while n1>0:
            r=n1%16
            if r>9:
                s= chr(55+r)
            else:
                s = str(r)
            hexa = s+hexa
            n1//=16
        print("The Hexa-Decimal Expansion of Decimal Value",n,"is",hexa)
        ch=input("Do you want to re-start the conversion?(yes/no):")

          
