N = int(input())
arr = list(map(int, input().split()))
S = int(input())
for i in range(N - 1):
    if S == 0:
        break
    max_v, idx = arr[i], i
    l = min(N, i + S + 1)
    for j in range(i + 1, l):
        if arr[j] > max_v:
            max_v, idx = arr[j], j
    S -= idx - i
    for k in range(idx, i, -1):
        arr[k], arr[k - 1] = arr[k - 1], arr[k]
print(*arr)
