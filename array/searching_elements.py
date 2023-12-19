# def search_array(arr,x):
#     n = len(arr)
#     flag = -1

#     for i in range(n):
#         if arr[i]==x:
#             flag = i
#             break
#     return flag





def search_array(arr , element):
    n = len(arr)
    for i in range(n):
        if arr[i] == element:
            return i






arr = list(map(int , input("Enter the arra elements suprated by space").split()))

x = int(input("enter search element"))

result = search_array(arr,x)

if result == -1 :
    print("Not Found in this array")
else:
    print(f"elments {x} is fount in index {result}")