import sys
input = sys.stdin.readline


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
s, e = 0, 0
for i in range(1, N):
    if lis[e] < arr[i]:
        lis[e + 1] = arr[i]
        e += 1
    else:
        idx = binary(s, e, arr[i])
        lis[idx] = arr[i]
print(e + 1)
