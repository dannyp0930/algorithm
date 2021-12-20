# 최대공약수
def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


# 최소공배수
def LCM(a, b):
    return int(a * b / GCD(a, b))


def solution(arr):
    answer = 1
    for num in arr:
        answer = LCM(answer, num)
    return answer
