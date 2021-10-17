from itertools import combinations

N, M = map(int, input().split())
arr = []
house = []
chicken = []
for r in range(N):
    tmp = list(map(int, input().split()))
    for c in range(N):
        if tmp[c] == 1:
            house.append((r, c))
        if tmp[c] == 2:
            chicken.append((r, c))
    arr.append(tmp)
store = int(len(chicken))


ans = 0xffffff
visit = [0] * store
result = list(combinations(chicken, M))
for lst in result:
    distance = 0
    for x, y in house:
        mini = 0xffffff
        for i, j in lst:
            num = abs(x - i) + abs(y - j)
            if mini > num:
                mini = num
        distance += mini
        if distance > ans:
            break
    if ans > distance:
        ans = distance
print(ans)
