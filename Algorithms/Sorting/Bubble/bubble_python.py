print("Please, input numbers to sort. Use space as delimeter. Press Enter when finished.\n")

# input numbers into array
arr = [int (i) for i in input().split(' ')]

# bubble sort algorithm

for i in range(0,len(arr)-1):
    for j in range(i,len(arr)):
        if arr[j]<arr[i]:
            arr[j],arr[i] = arr[i],arr[j]
            

# output of the sorted array
print(f"This is your sorted array:\n{arr}")