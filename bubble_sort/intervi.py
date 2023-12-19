
def continues(arr):
    n = len(arr)
    s = True
    for i in range(n):
        if i + 1 != arr[i]:
            s = False
    return s



arr = [1,2,3,4,5,6,7,8,9]

arr2 = [1,2,3,4,8,6,7,8,9]


print(continues(arr))

print(continues(arr2))


10111213141516171819
100101102103104105106107108109

