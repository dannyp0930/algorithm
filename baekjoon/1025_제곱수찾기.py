def is_square(n):
    return int(n ** 0.5) ** 2 == n

N, M = map(int, input().split())
table = [input() for _ in range(N)]
square_nums = set()
for r in range(N):
    for c in range(M):
        tmp = int(table[r][c])
        if is_square(tmp):
            square_nums.add(tmp)
        for rd in range(-N + 1, N):
            for cd in range(-M + 1, M):
                if rd == 0 and cd == 0: continue
                i, j = r, c
                tmp = table[i][j]
                while 0 <= i < N and 0 <= j < M:
                    i += rd
                    j += cd
                    if 0 > i or i >= N or 0 > j or j >= M: break
                    tmp += table[i][j]
                    if is_square(int(tmp)):
                        square_nums.add(int(tmp))
if square_nums:
    print(max(square_nums))
else:
    print(-1)
