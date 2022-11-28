def perm(n):
    if len(stack) == N:
        print(*stack)
        return
    for i in range(1, N + 1):
        if not visit[i]:
            visit[i] = 1
            stack.append(i)
            perm(n + 1)
            visit[i] = 0
            stack.pop()


N = int(input())
stack = []
visit = [0] * (N + 1)
perm(1)
