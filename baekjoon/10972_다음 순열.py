N = int(input())
arr = list(map(int, input().split()))
for i in range(N - 1, 0, -1):
    if arr[i] > arr[i - 1]:
        for j in range(N - 1, 0, -1):
            if arr[j] > arr[i - 1]:
                arr[j], arr[i - 1] = arr[i - 1], arr[j]
                arr = arr[:i] + sorted(arr[i:])
                print(*arr)
                exit()
print(-1)
