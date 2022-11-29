def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    return gcd(b, a % b)


for _ in range(int(input())):
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(1, arr[0] + 1):
        for j in range(i + 1, arr[0] + 1):
            ans += gcd(arr[i], arr[j])
    print(ans)
