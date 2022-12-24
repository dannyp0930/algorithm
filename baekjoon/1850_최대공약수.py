def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

A, B = map(int, input().split())
print('1' * gcd(A, B))