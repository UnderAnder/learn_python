def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
    else:
        gen_bin(M-1, prefix+"0")
        gen_bin(M-1, prefix+"1")
        
def generate_numbers(N:int, M:int, prefix=None):
    """ Генерирует все числа (с лидирующими незнащими нулями)
        в N-ричной система числения (N <= 10) длинны M
    """
    prefix = prefix or [] # если prefix == None, то пустой список
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

gen_bin(5)
generate_numbers(4, 3)