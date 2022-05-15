N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [0] * N
for i in range(N):
    tmp = 1
    for j in range(N):
        if i == j: continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            tmp += 1
    lst[i] = tmp
print(*lst)
