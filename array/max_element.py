def max_element(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

arr = [3,4,5,6,2,1,3]

print(max_element(arr))