def quick_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    left = []
    middle = []
    right = []
    for x in A: # с дополнительной памятью
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    k = 0
    quick_sort(left)
    quick_sort(right)
    for x in left+middle+right:
        A[k] = x
        k += 1       