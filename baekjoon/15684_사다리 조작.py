import sys


def check():
    for c in range(N):
        e = c
        for r in range(H):
            if graph[r][e]:
                e += 1
            elif e > 0 and graph[r][e - 1]:
                e -= 1
        if e != c:
            return False
    return True


def dfs(x, y, cnt):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3 or cnt >= ans:
        return
    for r in range(x, H):
        k = y if r == x else 0
        for c in range(k, N - 1):
            if not graph[r][c]:
                graph[r][c] = 1
                dfs(r, c + 2, cnt + 1)
                graph[r][c] = 0


input = sys.stdin.readline
N, M, H = map(int, input().split())
graph = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else - 1)
