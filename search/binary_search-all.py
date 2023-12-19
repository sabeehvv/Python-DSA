# def binary_search_all(arr,x):
#     n = len(arr)
#     left = 0
#     right = n-1

#     result = []

#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] == x:
#             result.append(mid)
#             i = mid -1
#             while i >= left and arr[i] == x:
#                 result.append(i)
#                 i -= 1

#             i = mid + 1
#             while i <= right and arr[i] == x:
#                 result.append(i)
#                 i += 1
#             return result
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result


# def binary_search_all(arr, x):
#     n = len(arr)
#     left = 0
#     right = n-1
#     result = []
#     while left < right:
#         mid = (left+right) // 2
#         if arr[mid] == x:
#             result.append(mid)
#             i = mid + 1
#             while i >= left and arr[i] == x:
#                 result.append(i)
#                 i += 1
#             i = mid - 1
#             while i <= right and arr[i] == x:
#                 result.append(i)
#                 i -= 1
#             return result
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return None

def binary_search_all(arr,x):
    n = len(arr)
    left = 0
    right = n - 1
    result = []
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if arr[mid] == x:
            result.append(mid)
            i = mid - 1
            while i >= left and arr[i] == x:
                result.append(i)
                i -= 1
            i = mid + 1
            while i <= right and arr[i] == x:
                result.append(i)
                i += 1
            return result
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return None


arr = [1, 2, 3, 4, 5, 5, 5, 6, 7]
x = 4
print(binary_search_all(arr, x))
