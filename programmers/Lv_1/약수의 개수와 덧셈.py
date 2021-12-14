def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        divisor = 0
        for n in range(1, num + 1):
            if not num % n:
                divisor += 1
        if divisor % 2:
            answer -= num
        else:
            answer += num
    return answer


# 수학적 풀이, 제곱수는 약수의 개수가 홀수개
def solution2(left, right):
    answer = 0
    for num in range(left, right + 1):
        if int(num ** 0.5) == num ** 0.5:
            answer -= num
        else:
            answer += num
    return answer
