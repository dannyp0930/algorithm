import sys
input = sys.stdin.readline


def dfs(r, c):
    if c == C - 1:
        return True
    for d in [-1, 0, 1]:
        nr, nc = r + d, c + 1
        if 0 <= nr < R and 0 <= nc < C:
            if not visit[nr][nc] and graph[nr][nc] == '.':
                visit[nr][nc] = 1
                if dfs(nr, nc):
                    return True
    return False


R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visit = [[0] * C for _ in range(R)]
cnt = 0
for sr in range(R):
    visit[sr][0] = 1
    if dfs(sr, 0):
        cnt += 1
print(cnt)
