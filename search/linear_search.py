def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = list(map (int , input("Enter Array elements sepreated by space").split()))
x = int(input("Enter number to search from array.."))


result = linear_search(arr, x)

if result == -1:
    print(f" Elements {x} is not present in this array")

else:
    print(f"Elements {x} is Present in index {result}")