# def factorial(n):
#     print(n)
#     if n == 0:
#         return 2
#     else:
#         s = n * factorial(n-1)
#         print("ss",s)
#         return s

# print(factorial(1))

def show(n):

    if n == 0:
        return 1

    return n*show(n-1)

print(show(5))
