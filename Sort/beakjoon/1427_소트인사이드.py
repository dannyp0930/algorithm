N = list(input())
count = [0] * 10
for num in N:
    count[int(num)] += 1
ans = ''
for i in range(9, -1, -1):
    ans += str(i) * count[i]
print(int(ans))
