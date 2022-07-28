from copy import deepcopy

def up(arr):
    for c in range(N):
        e = 0
        for r in range(1, N):
            if arr[r][c]:
                tmp, arr[r][c] = arr[r][c], 0
                if arr[e][c] == 0:
                    arr[e][c] = tmp
                elif arr[e][c] == tmp:
                    arr[e][c] = 2 * tmp
                    e += 1
                else:
                    e += 1
                    arr[e][c] = tmp
    return arr

def down(arr):
    for c in range(N):
        e = N - 1
        for r in range(N - 2, -1, -1):
            if arr[r][c]:
                tmp, arr[r][c] = arr[r][c], 0
                if arr[e][c] == 0:
                    arr[e][c] = tmp
                elif arr[e][c] == tmp:
                    arr[e][c] = 2 * tmp
                    e -= 1
                else:
                    e -= 1
                    arr[e][c] = tmp
    return arr

def left(arr):
    for r in range(N):
        e = 0
        for c in range(1, N):
            if arr[r][c]:
                tmp, arr[r][c] = arr[r][c], 0
                if arr[r][e] == 0:
                    arr[r][e] = tmp
                elif arr[r][e] == tmp:
                    arr[r][e] = 2 * tmp
                    e += 1
                else:
                    e += 1
                    arr[r][e] = tmp
    return arr

def right(arr):
    for r in range(N):
        e = N - 1
        for c in range(N - 2, -1, -1):
            if arr[r][c]:
                tmp, arr[r][c] = arr[r][c], 0
                if arr[r][e] == 0:
                    arr[r][e] = tmp
                elif arr[r][e] == tmp:
                    arr[r][e] = 2 * tmp
                    e -= 1
                else:
                    e -= 1
                    arr[r][e] = tmp
    return arr
 

def dfs(arr, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, arr[i][j])
        return
    dfs(up(deepcopy(arr)), cnt + 1)
    dfs(down(deepcopy(arr)), cnt + 1)
    dfs(left(deepcopy(arr)), cnt + 1)
    dfs(right(deepcopy(arr)), cnt + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(arr, 0)
print(ans)
