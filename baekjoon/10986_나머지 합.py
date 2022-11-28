N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr_m = [0] * M
sum = 0
cnt = 0
for i in range(N):
    sum += arr[i]
    tmp = sum % M
    if tmp == 0:
        cnt += 1
    arr_m[tmp] += 1
for j in range(M):
    if arr_m[j] != 0:
        cnt += (arr_m[j] * (arr_m[j] - 1)) // 2
print(cnt)
