def selection_sort(arr):
    n = len(arr)
    i = 0
    while i < n-1:
        small = i
        j = i+1
        while j < n:
            if arr[j] < arr[small]:
                small = j
            j += 1
        arr[i],arr[small] = arr[small],arr[i]
        i += 1
    return arr


arr = [3,45,66,55,44,33,22]
sort_array = selection_sort(arr)

print(sort_array)