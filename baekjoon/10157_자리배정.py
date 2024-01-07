dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

C, R = map(int, input().split())
K = int(input())
if K > C * R:
    print(0)
else:
    arr = [[0] * C for _ in range(R)]
    r, c, d = R - 1, 0, 0
    num = 1
    while num <= K:
        arr[r][c] = num
        if num == K:
            print(c + 1, R - r)
            break
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < R and 0 <= nc < C) or arr[nr][nc]:
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]
        r, c, num = nr, nc, num + 1
