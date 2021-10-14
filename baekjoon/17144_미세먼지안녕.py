dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dust():
    tmp_list = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c] >= 5:
                tmp = arr[r][c] // 5
                cnt = 0
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                        cnt += 1
                        tmp_list[nr][nc] += tmp
                tmp_list[r][c] -= tmp * cnt
    for r in range(R):
        for c in range(C):
            arr[r][c] += tmp_list[r][c]


# 시계 방향
dr1 = [0, -1, 0, 1]
dc1 = [1, 0, -1, 0]

# 반시계 방향
dr2 = [0, 1, 0, -1]
dc2 = [1, 0, -1, 0]


def clean(n, arr1, arr2):
    r, c = n, 1
    d = 0
    tmp = 0
    while 1:
        if r == n and c == 0:
            break
        nr, nc = r + arr1[d], c + arr2[d]
        if 0 <= nr < R and 0 <= nc < C:
            arr[r][c], tmp = tmp, arr[r][c]
            r, c = nr, nc
        else:
            d += 1


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
r1 = r2 = 0
for i in range(R):
    if arr[i][0] == -1:
        r1, r2 = i, i + 1
        break
for _ in range(T):
    dust()
    clean(r1, dr1, dc1)
    clean(r2, dr2, dc2)
ans = 0
for lst in arr:
    for num in lst:
        if num > 0:
            ans += num
print(ans)
