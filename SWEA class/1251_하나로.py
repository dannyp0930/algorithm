import sys
sys.stdin = open('1251.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    G = [[] for _ in range(N)]
    for i in range(N):
        x, y = X[i], Y[i]
        for j in range(i + 1, N):
            value = E * ((x - X[j]) ** 2 + (y - Y[j]) ** 2)
            G[i].append((j, value))
            G[j].append((i, value))
    key = [2000000000000] * N
    pi = [0] * N
    visit = [0] * N
    key[0] = 0
    for _ in range(N):
        u, min_val = 0, 2000000000000
        for i in range(N):
            if not visit[i] and min_val > key[i]:
                u, min_val = i, key[i]
        visit[u] = 1
        for v, w in G[u]:
            if not visit[v] and key[v] > w:
                key[v] = w
                pi[v] = u
    print('#{} {}'.format(T, round(sum(key))))
