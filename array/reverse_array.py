def reverse_array(arr):
    n = len(arr)-1
    reveesed_array = []
    for i in range(n,-1,-1):
        reveesed_array.append(arr[i])
    return reveesed_array



# arr = list(map (int,input("Enter array elements seprated by space").split()))

arr = [2,3,4,5,6,7,8,8,9]

result = reverse_array(arr)

print(result)