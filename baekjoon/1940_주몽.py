N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
s, e = 0, N - 1
while s < e:
    if arr[s] + arr[e] == M:
        ans += 1
        s += 1
        e -= 1
    elif arr[s] + arr[e] < M:
        s += 1
    else:
        e -= 1
print(ans)
