def bom(n, k):
    n = k * n * (1000 - n) / 1000
    return n

def bombyx1(n, k):
    i = 1
    n, k = int(n), float(k)
    if not 1 <= n <= 100 or not 1 <= k <= 4:
        return 84
    print(f"{i} {n:.2f}")
    while i < 100:
        n = bom(n, k)
        k += 0.01
        i += 1
        print(f"{i} {n:.2f}")
    return 0

def bombyx2(n, i0, i1):
    if not 1 <= n <= 100:
        return 84
    return 0
