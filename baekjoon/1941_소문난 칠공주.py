dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def comb(idx):
    global ans
    if len(stack) == 7:
        cnt = 0
        tmp = []
        for n in stack:
            x, y = n // 5, n % 5
            if arr[x][y] == 'Y':
                cnt += 1
            if cnt > 3:
                return
            tmp.append((x, y))
        Q = [(tmp[0][0], tmp[0][1], 1)]
        tmp.pop(0)
        while Q:
            r, c, t = Q.pop(0)
            if not tmp:
                ans += 1
                return
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if nr < 0 or nr >= 5 or nc < 0 or nc >= 5: continue
                if (nr, nc) not in tmp: continue
                Q.append((nr, nc, t + 1))
                tmp.remove((nr, nc))
        return
    for i in range(idx, 25):
        stack.append(i)
        comb(i + 1)
        stack.pop()


arr = [input() for _ in range(5)]
ans = 0
stack = []
comb(0)
print(ans)
