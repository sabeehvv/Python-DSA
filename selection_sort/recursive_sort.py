def recursive_selection(arr,n = None):
    if n is None:
        n = len(arr)
    if n == 1:
        return
    small = 0
    for i in range(1, n):
        if arr[i] < arr[small]:
            small = i
    arr[0],arr[small] = arr[small],arr[0]

    recursive_selection(arr[1:], n-1)
    return arr



arr = [12, 11, 13, 5, 6]
n = len(arr)
 
result = recursive_selection(arr,n)

print(result)