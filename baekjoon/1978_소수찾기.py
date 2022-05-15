def prime_number(n):
    if n == 1:
        return False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if not n % i:
            return False
    return True


N = int(input())
arr = map(int, input().split())
ans = 0
for num in arr:
    if prime_number(num):
        ans += 1
print(ans)
