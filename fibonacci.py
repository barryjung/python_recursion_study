def recursion(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return recursion(n-2)+recursion(n-1)


print(recursion(12))
print(recursion(5))
