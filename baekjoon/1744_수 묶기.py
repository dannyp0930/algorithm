N = int(input())
ans = 0
positive = []
negative = []
for _ in range(N):
    n = int(input())
    if n == 1:
        ans += 1
    elif n > 0:
        positive.append(n)
    else:
        negative.append(n)
positive.sort(reverse=True)
negative.sort()
if len(positive) % 2 == 1:
    ans += positive.pop()
if len(negative) % 2 == 1:
    ans += negative.pop()
for i in range(0, len(positive), 2):
    ans += positive[i] * positive[i + 1]
for i in range(0, len(negative), 2):
    ans += negative[i] * negative[i + 1]
print(ans)
