def determine():
    global ans
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if not arr[i][j][k]:
                    ans = 0
                    return
                if ans < arr[i][j][k]:
                    ans = arr[i][j][k]
    return


dr = [0, 0, 0, 0, 1, -1]
dc = [0, 0, -1, 1, 0, 0]
dh = [1, -1, 0, 0, 0, 0]
M, N, H = map(int, input().split())
arr = []
Q = [0] * (M * N * H)
front = rear = -1
for h in range(H):
    tmp = []
    for r in range(N):
        tmp.append(list(map(int, input().split())))
        for c in range(M):
            if tmp[r][c] == 1:
                rear += 1
                Q[rear] = (h, r, c)
    arr.append(tmp)
while front != rear:
    front += 1
    h, r, c = Q[front]
    Q[front] = 0
    for d in range(6):
        nh, nr, nc = h + dh[d], r + dr[d], c + dc[d]
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0:
            arr[nh][nr][nc] = arr[h][r][c] + 1
            rear += 1
            Q[rear] = (nh, nr, nc)
ans = 0
determine()
print(ans - 1)
