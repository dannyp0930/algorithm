S = input()
ans = 0
cur = S[0]
for i in range(1, len(S)):
    if cur != S[i]:
        ans += 1
        cur = S[i]
print((ans + 1) // 2)
