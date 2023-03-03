N, M = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 0, sum(arr)
max_t = max(arr)
while s <= e:
    m = (s + e) // 2
    if m < max_t:
        s = m + 1
        continue
    cnt, t = 1, 0
    for i in range(N):
        if t + arr[i] <= m:
            t += arr[i]
        else:
            cnt += 1
            t = arr[i]
    if cnt <= M:
        e = m - 1
    else:
        s = m + 1
print(s)
