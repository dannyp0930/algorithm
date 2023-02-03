def gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


A, B = map(int, input().split())
C, D = map(int, input().split())
num = A * D + B * C
den = B * D
GCD = gcd(num, den)
print(num // GCD, den // GCD)
