X = input()
Y = input()
N, M = len(X), len(Y)
i = 0
cnt = 0
while i <= N - M:
    if X[i : i + M] == Y:
        cnt += 1
        i += M
    else:
        i += 1
print(cnt)
