def backtrack(start, now, res, cnt):
    global ans
    if cnt == N:
        if arr[now][start]:
            res += arr[now][start]
            ans = min(ans, res)
        return
    if res > ans:
        return
    for i in range(N):
        if not visit[i] and arr[now][i]:
            visit[i] = 1
            backtrack(start, i, res + arr[now][i], cnt + 1)
            visit[i] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [0] * N
ans = float('inf')
for i in range(N):
    visit[i] = 1
    backtrack(i, i, 0, 1)
    visit[i] = 0
print(ans)
