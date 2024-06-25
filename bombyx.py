def calc_generation(n, k):
    return (k * n) * (1000 - n) / 1000

def further_generation(n, k, i0, i1):
    for _ in range(i0, i1 + 1):
        n = calc_generation(n, k)
        print(f"{k:.2f} {n:.2f}")

def grown_rate(n, k):
    n, k = int(n), float(k)
    if n < 0 or not (1.0 <= k <= 4.0):
        return 84
    print(f"1 {n:.2f}")
    for i in range(2, 101):
        n = calc_generation(n, k)
        if n < 0:
            n = 0
        print(f"{i} {n:.2f}")
    return 0

def init_and_end_generation(n, i0, i1):
    n, i0, i1 = int(n), int(i0), int(i1)
    tmp = n
    if n < 0 or not (1 < i0 <= i1):
        return 84
    for k in range(100, 401):
        for _ in range(1, i0 - 1):
            n = calc_generation(n, k / 100)
        if n < 0:
            n = 0
        further_generation(n, k / 100, i0, i1)
        n = tmp
    return 0
