def recursion(n):
    if n <= 1:
        return [1]
    pre_list = recursion(n-1)
    left_one = pre_list+[0]
    right_one = [0]+pre_list
    return [left_one[x]+right_one[x] for x in range(len(left_one))]


print(recursion(8))
