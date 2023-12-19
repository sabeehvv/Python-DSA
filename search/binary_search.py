# def binary_search(arr,x):
#     n = len(arr)
#     left = 0
#     right = n-1
#     while left < right:
#         mid = (left + right)//2
#         if arr[mid] == x:
#             return x
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1




def binary_search(arr,x):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid +1