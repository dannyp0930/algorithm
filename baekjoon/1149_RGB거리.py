#DP

def my_min(a, b):
    if a < b:
        return a
    else:
        return b


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    arr[i][0] += my_min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += my_min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += my_min(arr[i - 1][0], arr[i - 1][1])
ans = 1000 * N
for val in arr[N - 1]:
    if ans > val:
        ans = val
print(ans)
