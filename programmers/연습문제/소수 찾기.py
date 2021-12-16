# 일반적인 소수찾기
def prime1(number):
    for i in range(2, number):
        if not number % i:
            return False
    return True


def solution1(n):
    answer = 0
    for num in range(2, n + 1):
        if prime1(num):
            answer += 1
    return answer


# 제곱근 까지 판별하기
def prime2(number):
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return False
    return True


def solution2(n):
    answer = 0
    for num in range(2, n + 1):
        if prime2(num):
            answer += 1
    return answer


# 에라토스테네스의 체
def Eratos(number):
    nums = set(range(2, number + 1))
    for i in range(2, number + 1):
        if i in nums:
            nums -= set(range(i * 2, number + 1, i))
    return len(nums)
