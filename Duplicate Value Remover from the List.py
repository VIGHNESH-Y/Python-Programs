n=int(input("Enter the Number of Elements in the List:"))
l=[]
for i in range(n):
    l.append(int(input("Enter an element of the list : ")))
print("List Before ", l)
temp_list = []

for i in l:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list

print("List After removing duplicates ", my_list)
