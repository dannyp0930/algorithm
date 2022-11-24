N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
ans = 0
for i in range(N):
    w = arr[i] * (i + 1)
    ans = max(ans, w)
print(ans)
