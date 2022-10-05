N, L, W, H = map(int, input().split())
l, r = 0, max(L, W, H)
for _ in range(100):
    m = (l + r) / 2
    cnt = (L // m) * (W // m) * (H // m)
    if cnt >= N:
        l = m
    else:
        r = m
print('{0:.10f}'.format(r))
