def find(arr, target):
    global ans
    s, e = 0, N - 2
    while s < e:
        res = arr[s] + arr[e]
        if res == target:
            ans += 1
            return
        elif res < target:
            s += 1
        else:
            e -= 1


N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(N):
    find(A[:i] + A[i + 1:], A[i])
print(ans)
