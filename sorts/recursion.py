
def matryoshka(n):
    if n == 1:
        print("Матрешечка")
    else:
        print("Верх матрешки n =", n)
        matryoshka(n-1)
        print("Низ матрешки n =", n)
matryoshka(7)

def hanoi_tower(size, fromPole, toPole, withPole):
    if size == 0:
        print("moving disk from", fromPole, "to", toPole)
    hanoi_tower(size-1, fromPole, withPole, toPole)
    hanoi_tower(1, fromPole, toPole, withPole)
    hanoi_tower(size-1, withPole, toPole, fromPole)


hanoi_tower(4, "A", "B", "C")
