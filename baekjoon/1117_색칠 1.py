W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
fill = (x2 - x1) * (y2 - y1)
if f <= W // 2:
    if x1 < f:
        fill += (min(f, x2) - x1) * (y2 - y1)
else:
    if x1 < W - f:
        fill += (min(W - f, x2) - x1) * (y2 - y1)
ans = W * H - fill * (c + 1)
print(ans)
