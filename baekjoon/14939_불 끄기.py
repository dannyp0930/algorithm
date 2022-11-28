arr = []
for _ in range(10):
    tmp = list(input())
    for i in range(10):
        if tmp[i] == 'O':
            tmp[i] = True
        else:
            tmp[i] = False
    arr.append(tmp)
dr = [1, -1, 0, 0, 0]
dc = [0, 0, 0, 1, -1]
ans = 101
for f in range(1 << 10):
    copy = [arr[i][:] for i in range(10)]
    cnt = 0
    for i in range(10):
        if f & (1 << i):
            cnt += 1
            for d in range(5):
                nr, nc = dr[d], i + dc[d]
                if 0 <= nr < 10 and 0 <= nc < 10:
                    copy[nr][nc] = not copy[nr][nc]
    for r in range(1, 10):
        for c in range(10):
            if copy[r - 1][c]:
                cnt += 1
                for d in range(5):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < 10 and 0 <= nc < 10:
                        copy[nr][nc] = not copy[nr][nc]
    for i in range(10):
        if copy[9][i]:
            break
    else:
        ans = min(ans, cnt)
print(ans if ans < 101 else -1)