N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
idx = 0
for m in arr:
    if m[0] == K:
        break
    idx += 1
ans = 1
for m in arr:
    if arr[idx][1:] == m[1:]:
        break
    ans += 1
print(ans)
