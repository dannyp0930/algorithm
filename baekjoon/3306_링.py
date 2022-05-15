def GCD(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


N = int(input())
arr = list(map(int, input().split()))
for i in range(1, N):
    gcd = GCD(arr[0], arr[i])
    print(str(arr[0] // gcd) + "/" + str(arr[i] // gcd))
