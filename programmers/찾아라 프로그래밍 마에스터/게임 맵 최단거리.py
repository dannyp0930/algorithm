dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def solution(maps):
    R = len(maps)
    C = len(maps[0])
    visit = [[-1] * C for _ in range(R)]
    visit[0][0] = 1
    queue = [(0, 0)]
    while queue:
        r, c = queue.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if visit[nr][nc] != -1 or not maps[nr][nc]: continue
            visit[nr][nc] = visit[r][c] + 1
            queue.append((nr, nc))
    return visit[-1][-1]
