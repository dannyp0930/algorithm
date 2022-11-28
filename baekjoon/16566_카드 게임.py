def binary(s, e, t):
    while s < e:
        m = (s + e) // 2
        if cards[m] <= t:
            s = m + 1
        else:
            e = m
    return e


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    if b >= M:
        return
    a, b = find(a), find(b)
    parent[a] = b


N, M, K = map(int, input().split())
parent = [i for i in range(M)]
cards = sorted(list(map(int, input().split())))
order = list(map(int, input().split()))
for num in order:
    idx = binary(0, M, num)
    idx = find(idx)
    print(cards[idx])
    union(idx, idx + 1)
