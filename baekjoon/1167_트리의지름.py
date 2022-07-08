def dfs(s, c):
    visit[s] = c
    for e, w in graph[s]:
        if visit[e] == -1:
            dfs(e, c + w)
    

V = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr), 2):
        if arr[i] == -1:
            break
        graph[arr[0]].append((arr[i], arr[i + 1]))

# 1에서 가장 먼 노드 t 구하기
visit = [-1] * (V + 1)
dfs(1, 0)
t = 0
max_d = 0
for i in range(1, V + 1):
    if max_d < visit[i]:
        t, max_d = i, visit[i]

# t에서 가장 먼 노드 u 구하기
visit = [-1] * (V + 1)
dfs(t, 0)
u = 0
max_d = 0
for i in range(1, V + 1):
    if max_d < visit[i]:
        u, max_d = i, visit[i]

# t-u 거리가 지름
print(max_d)
