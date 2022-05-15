def backtrack(i, total):
    global cnt
    if i == N:
        return
    total += arr[i]
    if total == S:
        cnt += 1
    backtrack(i + 1, total)
    backtrack(i + 1, total - arr[i])


N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
backtrack(0, 0)
print(cnt)
