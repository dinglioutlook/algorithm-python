#有两个长度均为n的整数数组A和B，现在要从这两个数组中各抽出s个数字，分别构成两个新的数组C和D，要求数组C和D的内积最大。

# 思路:
# 排序后，备选的dot product 肯定是在数组的两端。(可以用反证法证明)
# 如果被选中，那么去掉这个数字。

def max_dot_product(A, B, s):
    A = sorted(A)
    B = sorted(B)

    result = 0
    while s != 0:
        candidate = [A[0]*B[0], A[-1]*B[-1], A[0]*B[-1], B[0]*A[-1]]
        max_value = max(candidate)
        result += max_value
        if candidate[0] == max_value:
            A, B = A[1:], B[1:]
        elif candidate[1] == max_value:
            A, B = A[:-1], B[:-1]
        elif candidate[2] == max_value:
            A, B = A[1:], B[:-1]
        else:
            A, B = A[:-1], B[1:]
        s -= 1
    
    return result

a = [-2,1,2]
b = [-2,-1,1]

print(max_dot_product(a, b, 2))