def GCD(a, b):
    if not a % b:
        return b
    return GCD(b, a % b)


A, B = map(int, input().split())
gcd = GCD(A, B)
print(gcd)
print(A * B // gcd)
