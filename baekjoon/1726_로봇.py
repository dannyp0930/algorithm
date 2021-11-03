# DFS/BFS

# 0: 동 1: 서 2: 남 3: 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs():
    Q.append((sr - 1, sc - 1, sd - 1))
    visit[sr - 1][sc - 1][sd - 1] = 1
    while Q:
        r, c, d = Q.pop(0)
        if r == er - 1 and c == ec - 1 and d == ed - 1:
            return visit[r][c][d]

        # 명령 1: Go k
        for k in range(1, 4):
            nr, nc = r + dr[d] * k, c + dc[d] * k
            # 궤도를 벗어나거나 벽을 만나는 경우 for문 종료
            if nr < 0 or nc < 0 or nr >= M or nc >= N or arr[nr][nc]: break

            # 방문 검사
            if not visit[nr][nc][d]:
                visit[nr][nc][d] = visit[r][c][d] + 1
                Q.append((nr, nc, d))

        # 명령 2: Turn dir
        if d == 0 or d == 1:  # 동, 서쪽을 바라보는 경우
            d1, d2 = 2, 3  # 남, 북쪽으로 회전
        else:  # 남, 북쪽을 바라보는 경우
            d1, d2 = 0, 1  # 동, 서쪽으로 회전

        # 방문 검사
        if not visit[r][c][d1]:
            visit[r][c][d1] = visit[r][c][d] + 1
            Q.append((r, c, d1))
        if not visit[r][c][d2]:
            visit[r][c][d2] = visit[r][c][d] + 1
            Q.append((r, c, d2))


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

# r: 행 c: 열 d: 방향
sr, sc, sd = map(int, input().split())  # 시작 좌표
er, ec, ed = map(int, input().split())  # 도착 좌표
visit = [[[0] * 4 for _ in range(N)] for _ in range(M)] # 방문 배열, visit[r][c][d]
Q = []
print(bfs() - 1)
for lst in visit:
    print(lst)
