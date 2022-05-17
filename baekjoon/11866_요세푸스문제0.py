N, K  = map(int, input().split())
queue = list(range(1, N + 1))
res = []
idx = K - 1
while queue:
    l = len(queue)
    if idx >= l:
        idx %= l
    res.append(str(queue.pop(idx)))
    idx += K - 1
print(f'<{", ".join(res)}>')
