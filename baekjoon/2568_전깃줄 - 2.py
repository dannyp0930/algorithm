import sys
input = sys.stdin.readline


def binary(s, e, t):
    while s < e:
        m = (s + e) // 2
        if lis[m] < t:
            s = m + 1
        else:
            e = m
    return e


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
lis = [0] * n
lis[0]= arr[0][1]
D = [0] * n
s, e = 0, 0
for i in range(1, n):
    if lis[e] < arr[i][1]:
        e += 1
        lis[e] = arr[i][1]
        D[i] = e
    else:
        D[i] = binary(s, e, arr[i][1])
        lis[D[i]] = arr[i][1]
ans = []
idx = max(D)
for i in range(n - 1, -1, -1):
    if D[i] == idx:
        ans.append(arr[i][1])
        idx -= 1
print(n - e - 1)
for i in range(n):
    if arr[i][1] not in ans:
        print(arr[i][0])
