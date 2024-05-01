def solution(order):
    answer = 0
    stack = []
    cur = 0
    for i in range(1, len(order) + 1):
        stack.append(i)
        while stack and stack[-1] == order[cur]:
            stack.pop()
            cur += 1
            answer += 1
    return answer