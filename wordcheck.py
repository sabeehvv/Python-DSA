def checkword(arr):
    n = len(arr)
    # print(set(arr))
    count = 0
    for i in range(n):
        for j in range(i):
            print("a",set(arr[i]))
            print("b",set(arr[j]))
            if set(arr[i]) == set(arr[j]):
                count += 1
    return count 


arr = ["aba","aab","abcd","bac","aabc"]

print(checkword(arr))