def recursion(n):
    if n <= 1:
        return [1]
    alist = recursion(n-1)+[0]
    blist = [0]+recursion(n-1)
    return [alist[x]+blist[x] for x in range(len(alist))]


print(recursion(8))
