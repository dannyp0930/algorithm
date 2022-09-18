N = int(input())
graph = [[0] * N for _ in range(N)]
for i in range(N):
    arr = input()
    for j in range(N):
        if arr[j] == 'Y':
            graph[i][j] = 1
cnt = 0
for i in range(N):
    tmp = 0
    for j in range(N):
        if graph[i][j] == 1:
            tmp += 1
        else:
            for k in range(N):
                if i == j or k == i or k == j: continue
                if graph[i][k] == 1 and graph[k][j] == 1:
                    tmp += 1
                    break
    cnt = max(cnt, tmp)
print(cnt)
