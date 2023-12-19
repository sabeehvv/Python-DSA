def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    
    right = [x for x in arr[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [3, 6, 2, 8, 1, 5, 9, 4, 7]
sorted_arr = quick_sort(arr)
print(sorted_arr)
