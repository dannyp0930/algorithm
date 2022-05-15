L = int(input())
arr = list(map(int, input().split()))
n = int(input())
max_num = max(arr)
ans = 0
for i in range(1, max_num):
    for j in range(i + 1, max_num + 1):
        if n < i or n > j:
            continue
        for num in arr:
            if num >= i and num <= j:
                break
        else:
            ans += 1
print(ans)
        