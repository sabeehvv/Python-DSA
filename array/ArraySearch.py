arr = input("Enter array values followed by space : ").split()
arr = [int(i)for i in arr]
print(arr)
search_input = int(input("Enter number to search :"))
found = False

for i in range(len(arr)):
    if arr[i] == search_input:
        found = True
        print("Number Found at index : ",i)
        break

if found ==False:
    print("Number is not Found in given array")



# arr1 = input("Enter array values seprated by space :").split()
# arr1 = [int(i)for i in arr]
# search = int(input("enter number to search :"))
# found1 = False
# for i in range(len(arr1)):
#     if arr1[i]==search:
#         found1 = True
#         print("Number found in index",i)
#         break

# if found1 == False:
#     print("Number not found")