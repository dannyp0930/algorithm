def perm_rep():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(1, N + 1):
        stack.append(i)
        perm_rep()
        stack.pop()


N, M = map(int, input().split())
visited = [0] * (N + 1)
stack = []
perm_rep()
