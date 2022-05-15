import sys
sys.stdin = open('1795.txt', 'r')

for T in range(1, int(input()) + 1):
    N, M, X = map(int, input().split())
    G1 = [[] for _ in range(N + 1)]
    G2 = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        G1[x].append((y, c))
        G2[y].append((x, c))
    D1 = [0xffffff] * (N + 1)
    Q1 = [X]
    D1[0] = D1[X] = 0
    while Q1:
        u = Q1.pop(0)
        for v, w in G1[u]:
            if D1[v] > D1[u] + w:
                D1[v] = D1[u] + w
                Q1.append(v)
    D2 = [0xffffff] * (N + 1)
    Q2 = [X]
    D2[0] = D2[X] = 0
    while Q2:
        u = Q2.pop(0)
        for v, w in G2[u]:
            if D2[v] > D2[u] + w:
                D2[v] = D2[u] + w
                Q2.append(v)
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = D1[i] + D2[i]
    print('#{} {}'.format(T, max(D)))
