import sys
input = sys.stdin.readline


def fish(j):
    for i in range(R):
        if arr[i][j]:
            res, arr[i][j] = arr[i][j][2], 0
            return res
    return 0


def move():
    global arr
    new = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c]:
                s, d, z = arr[r][c]
                nr, nc, d = get_next_pos(r, c, s, d)
                if not new[nr][nc] or new[nr][nc][2] < z:
                    new[nr][nc] = (s, d, z)
    arr = new
                

def get_next_pos(r, c, s, d):
    if d in [1, 2]:
        cycle = R * 2 - 2
        if d == 1:
            s += cycle - r
        else:
            s += r
        s %= cycle
        if s >= R:
            return cycle - s, c, 1
        return s, c, 2
    else:
        cycle = C * 2 - 2
        if d == 4:
            s += cycle - c
        else:
            s += c
        s %= cycle
        if s >= C:
            return r, cycle - s, 4
        return r, s, 3


R, C, M = map(int, input().split())
arr = [[0] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1
    arr[r][c] = (s, d, z)
ans = 0
for j in range(C):
    ans += fish(j)
    move()
print(ans)