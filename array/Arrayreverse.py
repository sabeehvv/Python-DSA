# arr = input("Enter elements of array separated by space: ").split()
# arr = [int(i) for i in arr]  # Convert input string to integer array
# arr = arr[::-1]  # Reverse array using slicing
# print("Reversed array is:", arr)

# arr = input("Enter Array followed by space ").split()
# arr = [int(i) for i in arr]
# arr = arr[::-1]
# print("array after reverse",arr)

# def reverse(arr):
#     n = len(arr)
#     start = 0
#     end = n - 1
#     while start < end :
#         arr[start],arr[end] = arr[end],arr[start]
#         start +=1
#         end -= 1
#     return arr

# arr = [2,3,4,5,6,7,8,9,0]

# print(reverse(arr))

# def reverse(arr):
#     n = len(arr)
#     l = int(n/2)
#     print(l)
#     for i in range(l):
#         arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
#     return arr

# def reverse(arr):
#     n = len(arr)
#     k = int(n/2)
#     for i in range(k):
#         arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
#     return arr


def reverse(arr):
    n = len(arr)
    k = int(n // 2)
    for i in range(k):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    return arr


arr = [2, 3, 4, 5, 6, 7, 8, 9, 0,4]

print(reverse(arr))
