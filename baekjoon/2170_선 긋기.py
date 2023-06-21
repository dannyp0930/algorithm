import sys
input = sys.stdin.readline


N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()
ans = 0
s, e = 0, 0
for x, y in lines:
    if s == 0 and e == 0:
        s, e = x, y
    elif e < x or y < s:
        ans += (e - s)
        s, e = x, y
    else:
        s, e = min(s, x), max(e, y)
ans += (e - s)
print(ans)