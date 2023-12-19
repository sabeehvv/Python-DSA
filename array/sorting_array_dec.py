# def sorting_array(arr):
#     n = len(arr)-1
#     for i in range(n-1):
#         for j in range(0,n-i):
#             if arr[j] < arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]

#     return arr


def sorting_array(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
    return arr


arr = list(map(int, input("enter array elements seprated by space").split()))

result = sorting_array(arr)

print(result)
