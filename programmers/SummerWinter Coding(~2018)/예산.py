# 함수 안에 함수, 재귀로 해결, 시간초과
def solution(d, budget):
    answer = 0
    N = len(d)

    def recursion(idx, cnt, p):
        nonlocal answer
        if p > budget:
            return
        if answer < cnt:
            answer = cnt
        for i in range(idx, N):
            recursion(i + 1, cnt + 1, p + d[i])

    recursion(0, 0, 0)

    return answer


# 수학적으로 풀면 된다. 오름 차순으로 더해가면서 가장 많을 때
def solution2(d, budget):
    answer = 0
    n = len(d)
    d.sort()
    tmp = 0
    for i in range(n):
        tmp += d[i]
        if tmp > budget:
            break
        answer += 1
    return answer
