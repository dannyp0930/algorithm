def perm():
    global ans
    if len(stack) == N:
        tmp = 0
        for i in range(0, N - 1):
            tmp += abs(stack[i] - stack[i + 1])
        ans = max(ans, tmp)
    for i in range(N):
        if not visit[i]:
            stack.append(arr[i])
            visit[i] = 1
            perm()
            stack.pop()
            visit[i] = 0


N = int(input())
arr = list(map(int, input().split()))
stack = []
visit = [0] * N
ans = 0
perm()
print(ans)
