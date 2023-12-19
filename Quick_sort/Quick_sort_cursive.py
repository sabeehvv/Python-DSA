# def squick_sort(arr):
#     n = len(arr)
#     left = []
#     right = []
#     if n <= 1:
#         return arr
#     pivot = arr[-1]
#     for i in range(n-1):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])

#     left = squick_sort(left)
#     right = squick_sort(right)

#     return left + [pivot] + right


def squick_sort(arr):
    n = len(arr)
    left = []
    right = []
    
    if n <= 1:
        return arr
    
    pivot = arr[-1]

    for i in range(n-1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left = squick_sort(left)

    right = squick_sort(right)

    return left + [pivot] + right


arr = [3, 6, 2, 8, 1, 5, 9, 4, 7]
sorted_arr = squick_sort(arr)
print(sorted_arr)