def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return


def insertions_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
        


arr = [2, 3, 4, 5, 1, 12, 3, 4]
sort = insertions_sort(arr)
print(sort)


def quick_sort(arr):
    n = len(arr)

    if n <= 0:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for i in range(n):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    left = quick_sort(left)

    right = quick_sort(right)

    return left + [pivot] + right