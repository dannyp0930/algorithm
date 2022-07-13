N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 100001
subset_sum = 0
e = 0
for s in range(N):
    while subset_sum < S and e < N:
        subset_sum += arr[e]
        e += 1
    if subset_sum >= S and ans > e - s:
        print(s, e - 1)
        ans = e - s
    subset_sum -= arr[s]
if ans == 100001:
    print(0)
else:
    print(ans)
