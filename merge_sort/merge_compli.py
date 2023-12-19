# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     merge_sort(left)
#     merge_sort(right)

#     i = j = k = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1

#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         arr[k] = right[j]
#         j += 1
#         k += 1

#     return arr


# def merge_sort1(arr):
#     n = len(arr)
#     if n <= 1:
#         return arr
#     mid = n // 2
#     L = arr[:mid]
#     R = arr[mid:]

#     merge_sort1(L)
#     merge_sort1(R)

#     i = j = k = 0

#     while i < len(L) and j < len(R):
#         if L[i] < R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1

#     while i < len(L):
#         arr[k] = L[i]
#         i += 1
#         k += 1

#     while j < len(R):
#         arr[k] = R[j]
#         j += 1
#         k += 1
    
#     return arr


def merge_sort(arr):
    n = len(arr)

    if n <= 1 :
        return arr
    
    mid = n // 2
    L = arr[mid:]
    R = arr[:mid]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i +=1 
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


arr = [3, 6, 2, 8, 1, 5, 9, 4, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)
