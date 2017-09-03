def divide_conquer(S, divide, combine):
    if len(S) == 1: return S
    L, R = divide(S)
    A, B = divide_conquer(L, divide, combine), divide_conquer(R, divide, combine)

    return combine(A, B)