def bom(n, k):
    n = k * n * (1000 - n) / 1000
    return n

def bombyx1(n, k):
    i = 1
    n, k = int(n), float(k)
    if not 1 <= n <= 100 or not 1 <= k <= 4:
        return 84
    print(f"{i} {n:.2f}")
    while k >= 1:
        n = bom(n, k)
        i += 1
        print(f"{i} {n:.2f}")
        k -= 0.01
    return 0

def bombyx2(n, i0, i1):
    return 0
