def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    print("lll",left)
    print("rrrr",right)

    return merge(left, right)

def merge(left, right):
    print("2laaa",left)
    print("2rrrrr",right)
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged



arr = [3, 6, 2, 8, 1, 5, 9, 4, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)