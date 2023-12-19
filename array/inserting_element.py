# def insert_element(arr,elemnt,index):
#     n = len(arr)

#     arr.append(None)
#     for i in range(n , index , -1):
#         arr [i] = arr[i-1]
#     arr[index] = elemnt
#     return arr


def insert_element(arr,element,index):
    arr.append(0)
    n = len(arr)
    for i in range(n - 1,index,-1):
        arr[i] = arr[i - 1]
    arr[index] = element
    return arr

arr = [4,5,6,8,2,3,4]

element = 33

index = 2

print(insert_element(arr,element,index))