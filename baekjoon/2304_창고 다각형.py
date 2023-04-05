N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
idx = high = 0
for i in range(N):
    if arr[i][1] > high:
        high = arr[i][1]
        idx = i
ans = 0
h = arr[0][1]
for i in range(idx):
    ans += h * (arr[i + 1][0] - arr[i][0])
    if h < arr[i + 1][1]:
        h = arr[i + 1][1]

h = arr[N - 1][1]
for i in range(N - 1, idx, - 1):
    ans += h * (arr[i][0] - arr[i - 1][0])
    if h < arr[i - 1][1]:
        h = arr[i - 1][1]
print(ans + high)
