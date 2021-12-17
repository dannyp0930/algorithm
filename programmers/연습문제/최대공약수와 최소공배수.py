# 최대공약수, 유클리드 호제법
def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


# 최소공배수
def LCM(a, b):
    return int(a * b / GCD(a, b))


def solution(n, m):
    return [GCD(n, m), LCM(n, m)]
