N, M = map(int, input().split())
arr = [input() for _ in range(N)]
result = N * M
for i in range(N - 7):
    for j in range(M - 7):
        tmp1 = tmp2 = 0
        # (i, j)가 B 기준
        for n in range(i, i + 8):
            for m in range(j, j + 8):
                if (n + m) % 2 == 0:
                    if arr[n][m] == "W":
                        tmp1 += 1
                    else:
                        tmp2 += 1
                else:
                    if arr[n][m] == "B":
                        tmp1 += 1
                    else:
                        tmp2 += 1
        result = min(tmp1, tmp2, result)
print(result)
