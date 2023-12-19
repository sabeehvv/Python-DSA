# def recursive_sort(arr,n):

#     if n <= 0:
#         return arr

#     recursive_sort(arr,n-1)
#     temp = arr[n-1]
#     j = n-2

#     while j >= 0 and arr[j] > temp:
#         arr[j+1] = arr[j]
#         j -= 1
#     arr[j+1] = temp
#     return arr

# arr = [12, 11, 13, 5, 6]
# n = len(arr)
 
# result = recursive_sort(arr, n)

# print(result)


def insertion_sort(arr , n):
    if  n <= 0 :
        return arr
    
    insertion_sort(arr, n-1)

    key = arr[n - 1]
    j = n-2

    while j >= 0 and key > arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
    return arr


arr = [12, 11, 13, 5, 6]
n = len(arr)
 
result = insertion_sort(arr, n)

print(result)