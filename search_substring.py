def equal(A, B): # O(N)
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True

def search_substring(s, sub):
    for i in range(0, len(s)-len(sub)+1):
        if equal(s[i:i+len(sub)], sub):
            print(i)
        
        