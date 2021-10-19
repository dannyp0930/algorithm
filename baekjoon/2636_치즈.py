# DFS/BFS

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs():
    while Q:
        r, c = Q.pop()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or nr >= R or nc >= C: continue
            if visit[nr][nc]: continue
            if arr[nr][nc] == 1:
                arr[nr][nc] = 2
            elif arr[nr][nc] == 0:
                visit[nr][nc] = 1
                Q.append((nr, nc))


def delete():
    global cheese
    for m in range(R):
        for n in range(C):
            if arr[m][n] == 2:
                arr[m][n] = 0
                cheese -= 1


R, C = map(int, input().split())
arr = []
cheese = 0
for i in range(R):
    tmp = list(map(int, input().split()))
    for j in range(C):
        if tmp[j]:
            cheese += 1
    arr.append(tmp)
cnt = 0
cheese_before = 0
while cheese:
    cheese_before = cheese
    Q = [(0, 0)]
    visit = [[0] * C for _ in range(R)]
    visit[0][0] = 1
    bfs()
    delete()
    cnt += 1
print(cnt)
print(cheese_before)
