# 진법 변환
string = '0123456789'
def convert(num, base):
    answer = ''
    q, r = divmod(num, base)
    if not q:
        return string[r]
    return convert(q, base) + string[r]


# 소수 판별
def is_prime(n):
    if n == 1:
        return False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if not n % i:
            return False
    return True


def solution(n, k):
    answer = 0
    number = convert(n, k)
    N = len(number)
    tmp = ''
    for i in range(N):
        if number[i] == '0':
            if tmp and is_prime(int(tmp)):
                answer += 1
            tmp = ''
        else:
            tmp += number[i]
    # 끝부분
    if tmp:
        if is_prime(int(tmp)):
            answer += 1
    return answer
