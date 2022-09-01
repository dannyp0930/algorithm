N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = 1000000000
ans = 0
for i in range(N - 1):
    if min_cost > costs[i]:
        min_cost = costs[i]
    ans += min_cost * roads[i]
print(ans)
