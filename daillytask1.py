# def check_string(s, t):
#     s_sting = set(s)
#     t_sting = set(t)

#     if s_sting == t_sting:
#         return True
#     else:
#         return False

# s = 'anagram'
# t = 'anagram'
# print(check_string(s, t))


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        small = i
        for j in range(i+1, n):
            if arr[j] < arr[small]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    return arr


arr = [3, 45, 66, 55, 44, 33, 22]
sort_array = selection_sort(arr)

print(sort_array)
