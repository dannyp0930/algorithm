import sys

input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def bfs(sr, sc):
    queue = [(0, sr, sc)]
    visit = [[0] * N for _ in range(N)]
    visit[sr][sc] = 1
    dist_list = []
    while queue:
        dist, r, c = queue.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                if arr[nr][nc] <= size:
                    queue.append((dist + 1, nr, nc))
                    visit[nr][nc] = 1
                    if 0 < arr[nr][nc] < size:
                        dist_list.append((dist + 1, nr, nc))
    dist_list.sort()
    return dist_list


N = int(input())
arr = []
sr = sc = 0
size = 2
eat_cnt = 0
time = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 9:
            sr, sc = i, j
    arr.append(tmp)
arr[sr][sc] = 0
while 1:
    target_list = bfs(sr, sc)
    if not target_list:
        break
    target = target_list[0]
    time += target[0]
    sr, sc = target[1], target[2]
    arr[sr][sc] = 0
    eat_cnt += 1
    if eat_cnt == size:
        size += 1
        eat_cnt = 0
print(time)
