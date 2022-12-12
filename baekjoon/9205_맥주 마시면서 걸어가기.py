for _ in range(int(input())):
    n = int(input())
    cord = [list(map(int, input().split())) for _ in range(n + 2)]
    visit = [0] * (n + 2)
    q = [0]
    visit[0] = 1
    while q:
        v = q.pop(0)
        if abs(cord[v][0] - cord[n + 1][0]) + abs(cord[v][1] - cord[n + 1][1]) <= 1000:
            print('happy')
            break
        for i in range(1, n + 1):
            if not visit[i]:
                if abs(cord[v][0] - cord[i][0]) + abs(cord[v][1] - cord[i][1]) <= 1000:
                    q.append(i)
                    visit[i] = 1
    else:
        print('sad')
