import sys
input = sys.stdin.readline


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1, m, s, d))
while K:
    while fireballs:
        r, c, m, s, d = fireballs.pop()
        nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
        graph[nr][nc].append((m, s, d))
    for r in range(N):
        for c in range(N):
            if len(graph[r][c]) > 1:
                sum_m, sum_s, odd, even, flag, cnt = 0, 0, 0, 0, 1, len(graph[r][c])
                while graph[r][c]:
                    m, s, d = graph[r][c].pop()
                    sum_m += m
                    sum_s += s
                    if d % 2:
                        odd += 1
                    else:
                        even += 1
                if not odd or not even:
                    flag = 0
                if sum_m >= 5:
                    for d in range(4):
                        fireballs.append((r, c, sum_m // 5, sum_s // cnt, 2 * d + flag))
            elif len(graph[r][c]):
                m, s, d = graph[r][c].pop()
                fireballs.append((r, c, m, s, d))
    K -= 1
print(sum([f[2] for f in fireballs]))
