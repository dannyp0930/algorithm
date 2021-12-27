def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(w,h):
    gcd = GCD(max(w, h), min(w, h))
    print(gcd)
    m, n = w // gcd, h // gcd
    return w * h - gcd * (m + n - 1)
