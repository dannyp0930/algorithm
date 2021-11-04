dr = [-2, -2, 2, 2, -1, 1, -1, 1]
dc = [-1, 1, -1, 1, -2, -2, 2, 2]


def bfs():
    global front, rear
    rear += 1
    Q[rear] = (sr, sc)
    visit[sr][sc] = 1
    while Q:
        front += 1
        r, c = Q[front]
        Q[front] = 0
        if r == er and c == ec:
            print(visit[r][c] - 1)
            return
        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if visit[nr][nc]: continue
            visit[nr][nc] = visit[r][c] + 1
            rear += 1
            Q[rear] = (nr, nc)


for T in range(int(input())):
    N = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    Q = [0] * N * N
    front = rear = -1
    visit = [[0] * N for _ in range(N)]
    bfs()
