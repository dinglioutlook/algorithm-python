
def quicksort(seq):
    if len(seq) <=1: return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)