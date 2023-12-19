# def delete_element(arr,index):
#     n = len(arr)-1
#     print(n)

#     for i in range(index,n):
#         arr[i]=arr[i+1]
#     arr.pop()
#     return arr

# arr = [3,4,6,2,3,4]

# index = 2

# print(delete_element(arr,index))

# def deleteElement(arr,index):
#     n = len(arr)-1
#     for i in range(index, n):
#         arr[i] = arr[i+1]
#     arr.pop()
#     return arr

# arr = [3,4,6,2,3,4]

# index = 4

# print(deleteElement(arr,index))


# def delete_element(arr, index):
#     n = len(arr) - 1

#     for i in range(index, n):
#         arr[i] = arr[i+1]

#     arr.pop()
#     return arr


# arr = [3, 4, 6, 2, 3, 4]

# index = 4

# print(delete_element(arr, index))


# def delete_element(arr,index):
#     n = len(arr)
#     for i in range(index ,n-1):
#         arr[i] = arr[i+1]
#     arr.pop()
#     return arr


def delete_element(arr, index):
    n = len(arr)
    for i in range(index , n - 1):
        arr[i] = arr[i+1]
    arr.pop()
    return arr

        
arr = [3, 4, 6, 2, 3, 4]

index = 4

print(delete_element(arr, index))

sortarr = sorted(arr)

print(sortarr)