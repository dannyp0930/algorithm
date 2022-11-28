import sys


# 최대 공약수
def gcd(a, b):
    if a > b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


# 최소 공배수
def lcm(a, b):
    return a * b // gcd(a, b)


# 카잉 달력
def kain(m, n, x, y):
    for i in range(x, lcm(m, n) + 1, m):
        tmp = i % n if i % n else n
        if tmp == y:
            return i
    return -1


input = sys.stdin.readline
for _ in range(int(input())):
    M, N, X, Y = map(int, input().split())
    print(kain(M, N, X, Y))
