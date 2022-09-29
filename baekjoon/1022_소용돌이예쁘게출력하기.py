import sys
input = sys.stdin.readline
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
r1, c1, r2, c2 = map(int, input().split())
arr = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
total = (c2 - c1 + 1) * (r2 - r1 + 1)
d = 0
cnt = 1
l = 1
r, c = 0, 0
max_num = 0
while total:
    for _ in range(2):
        for _ in range(l):
            if r1 <= r <= r2 and c1 <= c <= c2:
                arr[r - r1][c - c1] = cnt
                max_num = cnt
                total -= 1
            r += dr[d]
            c += dc[d]
            cnt += 1
        d = (d + 1) % 4
    l += 1
m = len(str(max_num))
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(str(arr[i][j]).rjust(m), end=' ')
    print()
