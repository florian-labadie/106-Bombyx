def bom(n, k):
    return (k * n) * (1000 - n) / 1000

def bom1(n, k, i0, i1):
    for i in range(i0, i1 + 1):
        n = bom(n, k)
        print(f"{k:.2f} {n:.2f}")

def bombyx1(n, k):
    n, k = float(n), float(k)
    if not (1 <= n <= 100) or not (1.0 <= k <= 4.0):
        return 84
    print(f"1 {n:.2f}")
    for i in range(2, 101):
        n = bom(n, k)
        print(f"{i} {n:.2f}")
    return 0

def bombyx2(n, i0, i1):
    n, i0, i1 = float(n), float(i0), float(i1)
    tmp = n
    if not (1 <= n <= 100) or not (0 < i0 <= i1):
        return 84
    for k in range(100, 401):
        for _ in range(int(i0)):
            n = bom(n, k/100)
        bom1(n, k/100, int(i0), int(i1))
        n = tmp
    return 0
