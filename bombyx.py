def bom(n, k):
    n = k * n * (1000 - n) / 1000
    return n

def bom1(n, k, i0, i1):
    while i0 < i1:
        i0 += 1
        n = bom(n, k)
        print(f"{k:.2f} {n:.2f}")
    return n
            
def bombyx1(n, k):
    i = 1
    n, k = float(n), float(k)
    if not 1 <= n <= 100 or not 1 <= k <= 4:
        return 84
    print(f"{i} {n:.2f}")
    while i < 100:
        n = bom(n, k)
        i += 1
        print(f"{i} {n:.2f}")
    return 0

def bombyx2(n, i0, i1):
    go = 0
    k = 1
    n, i0, i1 = float(n), float(i0), float(i1)
    if not 1 <= n <= 100 or not 0 < i0 < i1:
        return 84
    while k <= 4:
        while go < i0:
            n = bom(n, k)
            go += 1
        n = bom1(n, k, i0, i1)
        k += 0.01
        go = 1
    return 0
