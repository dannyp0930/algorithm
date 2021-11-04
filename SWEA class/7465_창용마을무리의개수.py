import sys
sys.stdin = open('7465.txt', 'r')


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    x, y = find_set(x), find_set(y)
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1


for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    p = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    ans = set()
    for i in range(1, N + 1):
        ans.add(find_set(i))
    print('#{} {}'.format(T, len(ans)))
