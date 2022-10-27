N = int(input())
k = int(input())
s, e = 1, N * N
ans = 0
while s <= e:
    m = (s + e) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(m // i, N)
    if cnt >= k:
        ans = m
        e = m - 1
    else:
        s = m + 1
print(ans)
