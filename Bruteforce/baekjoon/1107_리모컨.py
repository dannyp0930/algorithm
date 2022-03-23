N = int(input())
M = int(input())
if M:
    broken = list(input().split())
else:
    broken = []
ans = abs(100 - N)
for i in range(1000001):
    for n in str(i):
        if n in broken:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i - N))
print(ans)
