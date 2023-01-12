n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())
ans = 0
s, e = 0, n - 1
while s < e:
    tot = arr[s] + arr[e]
    if tot == x:
        ans += 1
        e -= 1
    elif tot < x:
        s += 1
    else:
        e -= 1
print(ans)
