def prefix_func(str):
    π = [0] * len(str)
    j = 0
    i = 1
    while i < len(str):
        if str[i] == str[j]:
            π[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                π[i] = 0
                i += 1
            else:
                j = π[j-1]
    print(*π)
    return π
    
def prefix_func2(str):
    π = [0] * len(str)
    for i in range(1, len(str)):
        p = π[i-1]
        while p > 0 and str[i] != str[p]:
            p = π[p-1]
        if str[i] == str[p]:
            p += 1
        π[i] = p
    print(*π)
    return π

        
prefix_func("abcabcd") # 0 0 0 1 2 3 0
prefix_func("abcabca") # 0 0 0 1 2 3 4 
prefix_func("abbaabbab") # 0 0 0 1 1 2 3 4 2      
prefix_func2("abcabcd") # 0 0 0 1 2 3 0
prefix_func2("abcabca") # 0 0 0 1 2 3 4 
prefix_func2("abbaabbab") # 0 0 0 1 1 2 3 4 2  