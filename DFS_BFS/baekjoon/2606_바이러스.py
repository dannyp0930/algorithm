N = int(input())
E = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(E):
    r, c = map(int, input().split())
    arr[r][c] = arr[c][r] = 1
visit = [0] * (N + 1)
v = 1
visit[v] = 1
stack = [0]
cnt = 0
while stack:
    for w in range(1, N + 1):
        if arr[v][w] == 1 and visit[w] == 0:
            stack.append(v)
            visit[w] = 1
            v = w
            cnt += 1
            break
    else:
        v = stack.pop()
print(cnt)
