def solution(n):
    answer = 1
    for i in range(1, n // 2 + 1):
        tmp = 0
        while tmp < n:
            tmp += i
            i += 1
        if tmp == n:
            answer += 1
    return answer
