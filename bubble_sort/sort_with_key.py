def sort_with_key(arr,key):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j][key] > arr[j+1][key]:
                arr[j][key],arr[j+1][key] = arr[j+1][key],arr[j][key]
    return arr


arr = [{'name':'sabeeh','age':33},{'name':'vishnu','age':21},{'name':'viveak','age':21},{'name':'ashraf','age':35},]

sort_key = sort_with_key(arr,'age')
print(sort_key)



