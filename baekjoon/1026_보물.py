N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i in range(N):
    ans += A[i] * B[i]
print(ans)
