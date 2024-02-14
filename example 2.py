def factorialn(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorialn(n-1)
def factorialk(k):
    if k == 0: # базовий випадок
        return 1
    else:
        return k * factorialk(k-1)
def factorialnk(n,k):
    p = (n-k)
    if  p == 0: # базовий випадок
        return 1
    else:
        return p * factorialk(p-1)

def number_of_groups(n, k):
    return factorialn/(factorialnk*factorialk)




