def calc(a, b):
    ans = 0
    for i in range(4):
        if a[i] != b[i]:
            ans += 1
    return ans


for _ in range(T := int(input())):
    N = int(input())
    arr = list(input().split())
    if N > 32:
        print(0)
    else:
        ans = float('inf')
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i == j or j == k or i == k: continue
                    cnt = 0
                    for d in range(4):
                        if arr[i][d] != arr[j][d]: cnt += 1
                        if arr[j][d] != arr[k][d]: cnt += 1
                        if arr[i][d] != arr[k][d]: cnt += 1
                    ans = min(ans, cnt)
        print(ans)
