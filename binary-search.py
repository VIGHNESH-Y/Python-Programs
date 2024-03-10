def binarySearch (lis, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if lis[mid] == x:
            return mid
        elif lis[mid] > x:
            return binarySearch(lis, l, mid-1, x)
        else:
            return binarySearch(lis, mid + 1, r, x)

    else:
        return -1

lis = []
n=int(input("Enter the Number of elements::"))
for i in range(n):
    lis.append(int(input("Enter the Value to be added in the list:")))
x = int(input("Enter the Value to be Found:"))
result = binarySearch(lis, 0, len(lis)-1, x)
if result != -1:
	print("Element",x," is present at index",result)
else:
    print ("The Element",x," is not present in list")
