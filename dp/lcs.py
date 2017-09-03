import functools
def rec_lcs(a, b):
    @memo
    def L(i, j):
        if min(i, j) < 0: return 0
        if a[i] == b[i]: return 1 + L(i-1, j-1)
        return max(L(i-1, j), L(i, j-1))
    return L(len(a)-1, len(b) -1)