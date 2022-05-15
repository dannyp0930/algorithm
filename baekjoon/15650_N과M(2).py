def comb(cnt):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(cnt, N + 1):
        stack.append(i)
        comb(i + 1)
        stack.pop()


N, M = map(int, input().split())
stack = []
comb(1)
