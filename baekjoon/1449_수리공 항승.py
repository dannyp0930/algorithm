N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s, e = arr[0], arr[0] + L
cnt = 1
for pos in arr:
    if s <= pos < e:
        continue
    else:
        s = pos
        e = pos + L
        cnt += 1
print(cnt)
