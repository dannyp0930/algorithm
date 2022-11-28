def comb(sr, sc, k, tot):
    global result
    if k == K:
        result = max(result, tot)
        return
    for r in range(sr, N):
        m = sc if r == sr else 0
        for c in range(m, M):
            if visit[r][c]: continue
            flag = True
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
                if visit[nr][nc]:
                    flag = False
                    break
            if flag:
                visit[r][c] = 1
                comb(r, c, k + 1, tot + arr[r][c])
                visit[r][c] = 0


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
result = -10000 * N * M
comb(0, 0, 0, 0)
print(result)
