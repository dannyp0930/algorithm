# 백트래킹, 중복조합

def comb_rep(cnt):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(cnt, N + 1):
        stack.append(i)
        comb_rep(i)
        stack.pop()


N, M = map(int, input().split())
stack = []
comb_rep(1)
