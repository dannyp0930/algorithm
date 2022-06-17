import sys


def power(a, b, c):
    if b == 1:
        return a % c
    tmp = power(a, b // 2, c)
    if b % 2:
        return tmp * tmp * a % c
    else:
        return tmp * tmp % c


input = sys.stdin.readline
A, B, C = map(int, input().split())
print(power(A, B, C))
