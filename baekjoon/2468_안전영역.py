# DFS/BFS

# 선형 큐
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(x, y, area):
    Q = [0] * N * N
    front = rear = -1
    rear += 1
    Q[rear] = (x, y)
    visit[x][y] = 1
    while front != rear:
        front += 1
        r, c = Q[front]
        Q[front] = 0
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if arr[nr][nc] < area or visit[nr][nc]: continue
            visit[nr][nc] = 1
            rear += 1
            Q[rear] = (nr, nc)


N = int(input())
arr = []
maximum = 1
minimum = 100
for _ in range(N):
    tmp = list(map(int, input().split()))
    for n in tmp:
        if maximum < n:
            maximum = n
        if minimum > n:
            minimum = n
    arr.append(tmp)

ans = 0
for k in range(minimum, maximum + 1):
    cnt = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= k and not visit[i][j]:
                bfs(i, j, k)
                cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)


# 라이브러리 사용
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(x, y, area):
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if arr[nr][nc] < area or visit[nr][nc]: continue
            visit[nr][nc] = 1
            Q.append((nr, nc))


N = int(input())
arr = []
maximum = 1
minimum = 100
for _ in range(N):
    tmp = list(map(int, input().split()))
    for n in tmp:
        if maximum < n:
            maximum = n
        if minimum > n:
            minimum = n
    arr.append(tmp)

ans = 0
for k in range(minimum, maximum + 1):
    cnt = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= k and not visit[i][j]:
                bfs(i, j, k)
                cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)
