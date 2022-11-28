dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
INF = float('inf')
cnt = 0
while 1:
    N = int(input())
    cnt += 1
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    visit = [[INF] * N  for _ in range(N)]
    q = [(0, 0)]
    visit[0][0] = graph[0][0]
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            s = visit[r][c] + graph[nr][nc]
            if visit[nr][nc] > s:
                q.append((nr, nc))
                visit[nr][nc] = s
    print('Problem {0}: {1}'.format(cnt, visit[N - 1][N - 1]))
