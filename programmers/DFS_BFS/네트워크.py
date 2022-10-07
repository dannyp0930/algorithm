def solution(n, computers):
    def bfs(visit, i):
        q = [i]
        while q:
            node = q.pop()
            visit[node] = 1
            for v in range(n):
                if v == node:
                    continue
                if not visit[v] and computers[node][v]:
                    q.append(v)
    answer = 0
    visit = [0] * n
    for i in range(n):
        if not visit[i]:
            bfs(visit, i)
            answer += 1
    return answer
