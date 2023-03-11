def binary(s, e, t):
    while s < e:
        mid = (s + e) // 2
        if lis[mid] < t:
            s = mid + 1
        else:
            e = mid
    return e


N = int(input())
A = list(map(int, input().split()))
lis = [0] * N
lis[0] = A[0]
s = e = 0
for i in range(1, N):
    if lis[e] < A[i]:
        lis[e + 1] = A[i]
        e += 1
    else:
        idx = binary(s, e, A[i])
        lis[idx] = A[i]
print(e + 1)
