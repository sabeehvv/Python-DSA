# def delete_duplicate(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(1+i,n):
#             if arr[i] == arr[j]:
#                 for k in range(i,n-1):
#                     arr[k]=arr[k+1]
#                 n = n-1
#     return arr[:n]


# arr = [2,3,4,4,6,3,4,4,]

# print(delete_duplicate(arr))

# def delete_duplicate(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n):
#             print(j)
#             if i != j and arr[i] == arr[j]:
#                 for k in range(j,n-1):
#                     arr[k] = arr[k+1]
#                 n -= 1
#     return arr[:n+2]


# def delete_duplicate(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(i+1,n):
#             if i != j and arr[i] == arr[j]:
#                 for k in range(j, n - 1):
#                     arr[k] = arr[k+1]
#                     n -= 1
#     return arr[:n]

def delete_duplicate(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                for k in range(j,n - 1):
                    arr[k] = arr[k+1]
                    n -= 1
    return arr[:n]

arr = [2,3,4,4,6,3,4,4,]

print(delete_duplicate(arr))
