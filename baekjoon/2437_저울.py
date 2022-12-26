N = int(input())
arr = list(map(int, input().split()))
arr.sort()
tot = 1
for num in arr:
    if num > tot:
        break
    tot += num
print(tot)
