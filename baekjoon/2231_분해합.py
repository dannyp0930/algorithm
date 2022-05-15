N = int(input())
ans = 0
for i in range(1, N):
    num = i
    tot = num
    while num:
        tot += num % 10
        num //= 10
    if tot == N:
        ans = i
        break
print(ans)
