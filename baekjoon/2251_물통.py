def pour(x, y):
    if not visit[x][y]:
        visit[x][y] = 1
        q.append((x, y))


A, B, C = map(int, input().split())
q = [(0, 0)]
visit = [[0] * (B + 1) for _ in range(A + 1)]
visit[0][0] = 1
ans = []
while q:
    a, b = q.pop(0)
    c = C - (a + b)
    if a == 0:
        ans.append(c)
    # A -> B
    w = min(a, B - b)
    pour(a - w, b + w)
    # A -> C
    w = min(a, C - c)
    pour(a - w, b)
    # B -> A
    w = min(A - a, b)
    pour(a + w, b - w)
    # B -> C
    w = min(b, C - c)
    pour(a, b - w)
    # C -> A
    w = min(A - a, c)
    pour(a + w, b)
    # C -> B
    w = min(B - b, c)
    pour(a, b + w)
ans.sort()
print(*ans)
