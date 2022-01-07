def solution(N, road, K):
    answer = 0
    G = [[0] * N for _ in range(N)]
    for a, b, c in road:
        if G[a - 1][b - 1]:
            G[a - 1][b - 1] = G[b - 1][a - 1] = min(G[a - 1][b - 1], c)
        else:
            G[a - 1][b - 1] = G[b - 1][a - 1] = c
    visit = [0] * N
    Q = [0]
    visit[0] = 1
    while Q:
        v = Q.pop()
        for u in range(1, N):
            if not G[v][u]: continue
            tmp = visit[v] + G[v][u]
            if visit[u] > tmp or not visit[u]:
                visit[u] = tmp
                Q.append(u)
    print(visit)
    for i in range(N):
        if visit[i] <= K + 1:
            answer += 1
    return answer
