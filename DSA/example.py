# print("hello")
# i = 0
# for i in range(30):
#     print("*")



def getConcatenation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    array1 = nums
    array2 = nums
    array = list(array1 + array2)
    return array
    


nums = [1,2,1]
arr = getConcatenation(nums)
print(arr)