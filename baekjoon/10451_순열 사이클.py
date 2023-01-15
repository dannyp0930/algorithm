import sys
sys.setrecursionlimit(10**6)


def dfs(n):
    visit[n] = 1
    v = arr[n]
    if not visit[v]:
        dfs(v)


for _ in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [0] * (N + 1)
    ans = 0
    for i in range(1, N + 1):
        if not visit[i]:
            dfs(i)
            ans += 1
    print(ans)
