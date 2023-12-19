# def binary_search(arr,x):
#     arr1 = sorted(arr)
#     print("Sorted array ",arr1)
#     left = 0
#     right = len(arr1) - 1

#     while left <= right:
#         mid = left+right // 2

#         if arr1[mid] == x:
#             return mid
#         elif arr1[mid] < x:
#             left = mid + 1
#         else:
#             right = mid -1

#     return -1


def binary_search(arr,x):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = list(map (int , input("Enter Array elements sepreated by space").split()))
x = int(input("Enter number to search from array.."))


result = binary_search(arr, x)

if result == -1:
    print(f" Elements {x} is not present in this array")

else:
    print(f"Elements {x} is Present in index {result}")