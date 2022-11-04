N = int(input())
arr = list(map(int, input().split()))
arr.sort()
s, e = 0, N - 1
sol = abs(arr[s] + arr[e])
res = (arr[s], arr[e])
while s < e:
    tmp = arr[s] + arr[e]
    if sol > abs(tmp):
        sol = abs(tmp)
        res = (arr[s], arr[e])
    if tmp < 0:
        s += 1
    else:
        e -= 1
print(*res)
