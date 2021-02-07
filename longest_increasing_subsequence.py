def lis(A:list): # Longest Increasing Subsequence
    """ finds the length of the greatest increasing subsequence"""
    F = [0]* (len(A) + 1)
    for i in range(1, len(A)+1):
        m = 0 # текущий максимум
        for j in range(1,i):
            if A[i-1] > A[j-1] and F[j] > m:  # тут нужно уменьшить индекс на 1 для массива А
                m = F[j]
        F[i] = m + 1
    print(F)
    return F[-1]
