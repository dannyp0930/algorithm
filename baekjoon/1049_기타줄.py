N, M = map(int, input().split())
package = 1000
single = 1000
for _ in range(M):
    a, b = map(int, input().split())
    package = min(package, a)
    single = min(single, b)
ans = min((N // 6 + 1) * package, N // 6 * package + N % 6 * single, N * single)
print(ans)
