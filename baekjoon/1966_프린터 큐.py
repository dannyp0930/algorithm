for _ in range(int(input())):
    N, M = map(int, input().split())
    document = list(map(int, input().split()))
    q = list(range(N))
    res = []
    cnt = 0
    while q:
        high = max(document)
        if document[q[0]] == high:
            document[q[0]] = 0
            res.append(q.pop(0))
        else:
            q.append(q.pop(0))

    print(res.index(M) + 1)