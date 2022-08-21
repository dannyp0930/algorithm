import sys
input = sys.stdin.readline


def pow(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    tmp = pow(n, k // 2)
    if k % 2:
        return tmp * tmp * n % mod
    else:
        return tmp * tmp % mod


mod = 1000000007
N = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += arr[i] * (pow(2, i) - pow(2, N - i - 1))
print(ans % mod)
