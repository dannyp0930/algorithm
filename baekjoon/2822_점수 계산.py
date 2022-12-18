arr = [(int(input()), i + 1) for i in range(8)]
arr.sort(reverse=True)
ans = 0
res = []
for i in range(5):
    ans += arr[i][0]
    res.append(arr[i][1])
res.sort()
print(ans)
print(*res)
