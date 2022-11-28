def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
parent = [i for i in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            union(i, j)
plan = list(map(int, input().split()))
connect = parent[plan[0] - 1]
for i in range(1, M):
    if parent[plan[i] - 1] != connect:
        print('NO')
        break
else:
    print('YES')