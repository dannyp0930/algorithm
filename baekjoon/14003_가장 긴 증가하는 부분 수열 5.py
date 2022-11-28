def binary(s, e, t):
    while s < e:
        mid = (s + e) // 2
        if lis[mid] < t:
            s = mid + 1
        else:
            e = mid
    return e


N = int(input())
arr = list(map(int, input().split()))
lis = [0] * N
lis[0] = arr[0]
D = [0] * N
s, e = 0, 0
for i in range(1, N):
    if lis[e] < arr[i]:
        e += 1
        lis[e] = arr[i]
        D[i] = e
    else:
        D[i] = binary(s, e, arr[i])
        lis[D[i]] = arr[i]
print(e + 1)
ans = []
idx = max(D)
for i in range(N - 1, -1, -1):
    if D[i] == idx:
        ans.append(arr[i])
        idx = D[i] - 1
print(*ans[::-1])