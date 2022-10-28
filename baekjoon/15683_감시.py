from copy import deepcopy


def watch(r, c, dir, tmp):
    for d in dir:
        nr, nc = r, c
        while 1:
            nr += dr[d]
            nc += dc[d]
            if 0 <= nr < N and 0 <= nc < M and tmp[nr][nc] != 6:
                if tmp[nr][nc] == 0:
                    tmp[nr][nc] = 7
            else:
                break


def dfs(arr, cnt):
    global ans
    if cnt == cam_cnt:
        res = 0
        for lst in arr:
            res += lst.count(0)
        ans = min(ans, res)
        return
    tmp = deepcopy(arr)
    r, c, cam = cams[cnt]
    for dir in cam_dir[cam]:
        watch(r, c, dir, tmp)
        dfs(tmp, cnt + 1)
        tmp = deepcopy(arr)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cam_dir = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 3], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    [[0, 1, 2, 3]]
]
N, M = map(int, input().split())
arr = []
cams = []
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for j in range(M):
        if tmp[j] != 0 and tmp[j] != 6:
            cams.append((i, j, tmp[j]))
cam_cnt = len(cams)
ans = int(1e9)
dfs(arr, 0)
print(ans)
