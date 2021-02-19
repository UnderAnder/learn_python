def prefix_func(str):
    π = [0] * len(str)
    for i in range(1, len(str)):
        p = π[i-1]
        while p > 0 and str[i] != str[p]:
            p = π[p-1]
        if str[i] == str[p]:
            p += 1
        π[i] = p
    return π

def kmp(str, sub):
    k = 0
    l = 0
    p = prefix_func(str)
    while k < len(str) and l < len(sub):
        if str[k] == sub[l]:
            k += 1
            l += 1
            if l == len(sub):
                return True
        else:
            if l ==0:
                k += 1
                if k == len(str):
                    return False
            else:
                l = p[l-1]
            
print(kmp("abcabeabcabcabd", "abcabd"))