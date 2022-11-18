H, W = map(int, input().split())
block = list(map(int, input().split()))
ans = 0
for i in range(1, W - 1):
    left = max(block[:i])
    right = max(block[i:])
    height = min(left, right)
    if block[i] < height:
        ans += height - block[i]
print(ans)
