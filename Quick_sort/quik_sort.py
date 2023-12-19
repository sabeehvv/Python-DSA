def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:

            i = i+1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1

def quick_sort(arr, low, high):
    if low < high:

        par = partition(arr, low, high)

        quick_sort(arr, low, par - 1)

        quick_sort(arr, par + 1, high)


arr = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(arr)

size = len(arr)

quick_sort(arr, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(arr)