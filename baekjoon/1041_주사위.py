N = int(input())
arr = list(map(int, input().split()))
if N == 1:
    print(sum(arr) - max(arr))
else:
    s1 = 50
    s2 = 100
    s3 = 150
    for i in range(6):
        s1 = min(s1, arr[i])
        for j in range(i + 1, 6):
            if i + j == 5: continue
            s2 = min(s2, arr[i] + arr[j])
            for k in range(j + 1, 6):
                if (j + k == 5 or k + i == 5): continue
                s3 = min(s3, arr[i] + arr[j] + arr[k])
    res = 4 * s3 + (8 * N - 12) * s2 + (5 * N * N - 16 * N + 12) * s1
    print(res)
