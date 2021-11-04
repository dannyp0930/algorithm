def perm():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(1, N + 1):
        if i not in stack:
            stack.append(i)
            perm()
            stack.pop()


N, M = map(int, input().split())
visited = [0] * (N + 1)
stack = []
perm()
