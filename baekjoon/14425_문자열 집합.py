N, M = map(int, input().split())
S = {input(): 0 for _ in range(N)}
ans = 0
for _ in range(M):
    ch = input()
    if ch in S:
        ans += 1
print(ans)