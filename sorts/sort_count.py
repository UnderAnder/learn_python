N = [1, 2, 3, 5, 2, 7, 6, 0, 9, 9, 2, 8, 6, 3, 4, 1, 5, 2, 3, 6, 7, 6, 6, 6, 1, 3, 5, 2]
F = [0]*10
for i in N:
    F[i] += 1
for digit in range(10):
    print(digit,":", F[digit])