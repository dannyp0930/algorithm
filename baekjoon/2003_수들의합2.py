N, M = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 0, 1
ans = 0
while e <= N and s <= e:
    tot = sum(arr[s:e])
    if tot == M:
        ans += 1
        e += 1
    elif tot < M:
        e += 1
    else:
        s += 1
print(ans)
