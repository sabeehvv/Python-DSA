def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr
    
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]
    print("l",left)
    print("r",right)

    left = merge_sort(left)

    right = merge_sort(right)

    merged = []

    i,j = 0,0  

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            j += 1
    print("left",left)
    print("right",right)
    print("merged",merged)

    merged += left[i:]

    merged += right[j:] 

    return merged


arr = [3, 6, 2, 8, 1, 5, 9, 4, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)



