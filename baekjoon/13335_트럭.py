n, w, L = map(int, input().split())
arr = list(map(int, input().split()))
q = [0] * w
time = 0
while q:
    time += 1
    q.pop(0)
    if arr:
        if sum(q) + arr[0] <= L:
            q.append(arr.pop(0))
        else:
            q.append(0)
print(time)
