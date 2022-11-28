N = int(input())
ans, cnt = 0, 1
while cnt <= N:
    ans += (N - cnt + 1)
    cnt *= 10
print(ans)
