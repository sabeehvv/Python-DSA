import time

def binary_search_recuirsion(arr,left,rigt,x):
    while left <= rigt:
        mid = (left + rigt) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search_recuirsion(arr,mid+1,rigt,x)
        else:
            binary_search_recuirsion(arr,left,mid-1,x)
    return -1


def binary_search(arr,x):
    n = len(arr)-1
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = list(range(10000000))

x = 9999999
# print(arr)

start = time.perf_counter()
result1 = binary_search_recuirsion(arr, 0, len(arr)-1, x)
end = time.perf_counter()
print("Recursive binary search result:", result1)
print("Time taken by recursive binary search:", end-start)


start = time.perf_counter()
result2 = binary_search(arr, x)
end = time.perf_counter()
print("Iterative binary search result:", result2)
print("Time taken by iterative binary search:", end-start)

