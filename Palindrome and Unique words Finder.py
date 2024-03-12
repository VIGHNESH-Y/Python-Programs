ch="yes"
while ch=="yes":
    userinput=input('Enter word sequence:')
    string = userinput.split()
    temp = [i[::-1] for i in string]
    unique = 0
    palindrome = 0
    for i in range(len(temp)):
        if temp[i] == string[i]:
            palindrome += 1
        else:
            unique += 1

    print('There are', palindrome, 'Palindromes, and', unique, 'unique words')
    ch=input("Do you want to continue?")
