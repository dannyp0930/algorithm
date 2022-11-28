import sys


def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
dir = { 'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1] }
N, M = map(int, input().split())
K = N * M
arr = [input().rstrip() for _ in range(N)]
parent = [i for i in range(K)]
for k in range(K):
    r, c = k // M, k % M
    move = dir[arr[r][c]]
    nr, nc = r + move[0], c + move[1]
    nk = nc + nr * M
    union(k, nk)
ans = 0
for i in range(K):
    if i == find(parent[i]):
        ans += 1
print(ans)
