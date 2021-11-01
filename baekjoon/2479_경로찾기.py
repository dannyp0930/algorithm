def dfs(v):
    global result
    if v == B:
        result = stack[:]
        return
    else:
        for w in G[v]:
            stack.append(w)
            dfs(w)
            stack.pop()


N, K = map(int, input().split())
num = [''] + [input() for _ in range(N)]
A, B = map(int, input().split())
G = [[] for _ in range(N + 1)]
visit = [0xfffff] * (N + 1)
visit[A] = 1
Q = [A]
while Q:
    i = Q.pop(0)
    for j in range(1, N + 1):
        if i == j : continue
        distance = 0
        for n1, n2 in zip(num[i], num[j]):
            if n1 != n2:
                distance += 1
            if distance > 1:
                break
        if distance == 1:
            if visit[j] > visit[i] + 1:
                visit[j] = visit[i] + 1
                G[i].append(j)
                Q.append(j)

result = [-1]
stack = [A]
dfs(A)
print(*result)
