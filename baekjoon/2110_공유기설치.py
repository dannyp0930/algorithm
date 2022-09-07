N, C = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
s, e = 1, arr[N - 1] - arr[0]
while s <= e:
    m = (s + e) // 2
    cur = arr[0]
    cnt = 1
    for i in range(1, N):
        if arr[i] >= cur + m:
            cnt += 1
            cur = arr[i]
    if cnt >= C:
        s = m + 1
    else:
        e = m - 1
print(e)
