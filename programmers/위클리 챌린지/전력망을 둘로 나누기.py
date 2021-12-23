def bfs(start, visit, graph):
    Q = [start]
    result = 1
    visit[start] = 1
    while Q:
        now = Q.pop()
        for i in graph[now]:
            if visit[i]: continue
            result += 1
            Q.append(i)
            visit[i] = 1
    return result


def solution(n, wires):
    answer = n
    G = [[] for _ in range(n + 1)]
    for w1, w2 in wires:
        G[w1].append(w2)
        G[w2].append(w1)
    for s, c in wires:
        visit = [0] * (n + 1)
        visit[c] = 1
        tmp = bfs(s, visit, G)
        print(tmp, n - tmp)
        answer = min(answer, abs(tmp - (n - tmp)))
    return answer
