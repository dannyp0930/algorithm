N = int(input())
arr = list(map(int, input().split()))
res = [0] * N
for i in range(N):
    idx = arr[i]
    cnt = 0
    for j in range(N):
        if res[j] == 0 and cnt == idx:
            res[j] = i + 1
            break
        elif res[j] == 0:
            cnt += 1
print(*res)
