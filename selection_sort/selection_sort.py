def selction_sort(arr):
    n = len(arr)
    for i in range(n):
        small = i
        for j in range(i+1, n):
            if arr[j] < arr[small]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        small = i
        for j in range(i+1,n):
            if arr[small] > arr[j]:
                small = j
        arr[small] , arr[i] = arr[i] , arr[small]
    return arr



arr = [3, 45, 66, 55, 44, 33, 22]
sort_array = selection_sort(arr)

print(sort_array)
