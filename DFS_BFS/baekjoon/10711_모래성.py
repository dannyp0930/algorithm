# 8 방향, 시계방향으로
dh = [-1, -1, 0, 1, 1, 1, 0, -1]
dw = [0, 1, 1, 1, 0, -1, -1, -1]
H, W = map(int, input().split())
arr = [[] for _ in range(H)]
Q = [0] * H * W
front = rear = - 1
visit = [[0] * W for _ in range(H)]
for i in range(H):
    tmp = input()
    for j in range(W):
        if tmp[j] == '.':
            arr[i].append(0)
            rear += 1
            Q[rear] = (i, j)    # 파도가 치는 부분을 Q에 추가
        else:
            arr[i].append(int(tmp[j]))
ans = 0
while front != rear:
    front += 1
    h, w = Q[front]
    Q[front] = 0
    for d in range(8):
        nh, nw = h + dh[d], w + dw[d]
        if nh < 0 or nw < 0 or nh >= H or nw >= W: continue
        if arr[nh][nw]: # 파도 주변에 모래성이 있다면
            arr[nh][nw] -= 1    # 모래성을 한개씩 제거 (한번 제거하면 다음 반복문에서 제거되지 않는다)
            if not arr[nh][nw]: # 반복문에서 모래가 모두 제거 된다면
                visit[nh][nw] = visit[h][w] + 1 # 걸린 시간을 기록하고
                rear += 1
                Q[rear] = (nh, nw)  # Q에 추가
                if ans < visit[nh][nw]:
                    ans = visit[nh][nw]
print(ans)
