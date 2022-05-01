# 최대공약수
def GCD(a, b):
    while b:
        t = a % b
        a, b = b, t
    return a


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A * B // GCD(A, B))
