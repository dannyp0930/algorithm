N, K = map(int, input().split())
ans = 1
for i in range(N, N - K, -1):
    ans *= i
for j in range(K, 0, -1):
    ans /= j
print(int(ans))