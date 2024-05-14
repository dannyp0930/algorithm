from collections import deque


def solution(maps):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    def bfs(i, j):
        q = deque([(i, j)])
        visit[i][j] = 1
        res = int(maps[i][j])
        while q:
            r, c = q.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if visit[nr][nc] or maps[nr][nc] == "X":
                    continue
                visit[nr][nc] = 1
                q.append((nr, nc))
                res += int(maps[nr][nc])
        return res

    ans = []
    R = len(maps)
    C = len(maps[0])
    visit = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if not visit[i][j] and maps[i][j] != "X":
                ans.append(bfs(i, j))
    if not len(ans):
        return [-1]
    ans.sort()
    return ans
