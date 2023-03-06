dl = [1, -1, 0, 0, 0, 0]
dr = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]

while 1:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break
    arr = []
    start = end = (0, 0, 0)
    for l in range(L):
        floor = []
        for r in range(R):
            tmp = list(input())
            for c in range(C):
                if tmp[c] == 'S':
                    start = (l, r, c)
                    tmp[c] = '.'
                if tmp[c] == 'E':
                    end = (l, r, c)
                    tmp[c] = '.'
            floor.append(tmp)
        blank = input()
        arr.append(floor)
    q = [start]
    arr[start[0]][start[1]][start[2]] = 0
    while q:
        l, r, c = q.pop(0)
        for d in range(6):
            nl, nr, nc = l + dl[d], r + dr[d], c + dc[d]
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if arr[nl][nr][nc] == '.':
                    arr[nl][nr][nc] = arr[l][r][c] + 1
                    q.append((nl, nr, nc))
    cnt = arr[end[0]][end[1]][end[2]]
    if cnt == '.':
        print('Trapped!')
    else:
        print(f'Escaped in {cnt} minute(s).')
