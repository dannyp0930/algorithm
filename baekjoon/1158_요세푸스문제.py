N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]
res = []
idx = 0
while arr:
    l = len(arr)
    idx += K - 1
    idx %= l
    res.append(arr.pop(idx))
print('<' + ', '.join(map(str, res)) + '>')
