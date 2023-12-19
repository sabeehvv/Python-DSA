# def factorial(n):
#     if n <= 1:
#         return n
#     return n * factorial(n-1)

# print(factorial(5))


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linked_list:
#     def __init__(self):
#         self.head = None

#     def add_node(self,data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#         current_node = self.head
#         while current_node.next is not None:
#             current_node = current_node.next
#         current_node.next = new_node

#     def remove_dublicate(self):
#         if self.head is None:
#             return
#         current_node = self.head
#         while current_node is not None:
#             new_node = current_node
#             while new_node.next is not None:
#                 if new_node.data == new_node.next.data:
#                     new_node.next = new_node.next.next
#                 new_node = new_node.next
#             current_node = current_node.next


# def removeDuplicates(nums):
#     n = len(nums)
#     for i in range(n-1):
#         if nums[i] == nums[i+1]:
#             for j in range(i,n-1):
#                 nums[j] = nums [j+1]
#                 i -= 1
#                 n -= 1
#     return nums[:n]
    

# arr = [1,2,2,3]

# print(removeDuplicates(arr))


s = max(6,3,10,44)

print(s)

