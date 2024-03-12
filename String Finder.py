fullstring =input("Enter the string for which you want to check:")
substring = input("Enter the Substring for which you have to find from the main string:")
if substring in fullstring:
    print (substring,"Is present in",fullstring)
else:
    print (substring,"Is  not present in",fullstring)

