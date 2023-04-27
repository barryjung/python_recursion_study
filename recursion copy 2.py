# def recursion(n):
#     print(n)
#     recursion(n+1)


# recursion(1)
# import sys
# print(sys.getrecursionlimit())


# def recursion(n):
#     if n <= 0:
#         return 1
#     return n * recursion(n-1)


# print(recursion(5))

def recursion(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return recursion(n-2)+recursion(n-1)


print(recursion(5))
