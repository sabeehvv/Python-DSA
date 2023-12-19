# def sort_array(arr):
#     swapped = True
#     itteration = 0
#     n = len(arr)
#     while(swapped):
#         swapped = False
#         for i in range(n - 1):
#             if arr[i] > arr[i+1]:
#                 arr[i],arr[i+1] = arr[i+1],arr[i]
#                 swapped = True
#         itteration += 1
#     print(itteration)
#     return arr

def sort_array(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                


arr = [2, 3, 4, 5, 1, 12, 3, 4]
sort = sort_array(arr)
print(sort)


def sort_array(arr):
    swapped = True
    itteration = 0
    n = len(arr)
    while (swapped):
        swapped = False
        for i in range(n - itteration - 1):
            if arr[i] < arr[i+1]:
                swapped = True
        itteration += 1
    print(itteration)
    return arr


# def sort_with_bool(arr):
#     swapped = True
#     n = len(arr)
#     while (swapped):
#         swapped = False
#         for i in range(n - 1):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                 swapped = True
#         itteration += 1
