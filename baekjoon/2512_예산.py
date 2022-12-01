N = int(input())
budget = list(map(int, input().split()))
M = int(input())
start = 1
end = max(budget)
while start <= end:
    mid = (start + end) // 2
    tot = 0
    for b in budget:
        if b <= mid:
            tot += b
        else:
            tot += mid
    if tot > M:
        end = mid - 1
    else:
        start = mid + 1
print(end)
