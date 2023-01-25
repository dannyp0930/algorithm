N = int(input())
arr = [input() for _ in range(N)]
r = 0
c = 0
for i in range(N):
    r_cnt = c_cnt = 0
    for j in range(N):
        if arr[i][j] == '.':
            r_cnt += 1
        else:
            r_cnt = 0
        if arr[j][i] == '.':
            c_cnt += 1
        else:
            c_cnt = 0
        if r_cnt == 2:
            r += 1
        if c_cnt == 2:
            c += 1
print(r, c)
