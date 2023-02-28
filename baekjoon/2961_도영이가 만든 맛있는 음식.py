def backtrack(sour, bitter, cnt, idx):
    global ans
    if cnt:
        ans = min(ans, abs(sour - bitter))
    if idx == N:
        return
    backtrack(sour * arr[idx][0], bitter + arr[idx][1], cnt + 1, idx + 1)
    backtrack(sour, bitter, cnt, idx + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = float("inf")
backtrack(1, 0, 0, 0)
print(ans)
