for _ in range(T := int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    for i in range(N - 2):
        ans = max(ans, arr[i + 2] - arr[i])
    print(ans)