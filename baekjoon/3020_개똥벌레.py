# 이분탐색
def binary(arr, target):
    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] >= target:
            e -= 1
        else:
            s += 1
    return s


N, H = map(int, input().split())
top = []
bot = []
for i in range(N):
    h = int(input())
    if i % 2:
        top.append(h)
    else:
        bot.append(h)
top.sort()
bot.sort()
ans = N
cnt = 0
for h in range(1, H + 1):
    t, b = binary(top, H - h + 1), binary(bot, h)
    tmp = N - (t + b)
    if tmp < ans:
        ans = tmp
        cnt = 1
    elif tmp == ans:
        cnt += 1
print(ans, cnt)

# 누적합
N, H = map(int, input().split())
up = [0] * (H + 1)
down = [0] * (H + 1)
for i in range(N):
    h = int(input())
    if i % 2:
        up[h] += 1
    else:
        down[h] += 1
for i in range(H - 1, 0, -1):
    up[i] += up[i + 1]
    down[i] += down[i + 1]
ans = N
cnt = 0
for i in range(1, H + 1):
    if ans > up[H - i + 1] + down[i]:
        ans = up[H - i + 1] + down[i]
        cnt = 1
    elif ans == up[H - i + 1] + down[i]:
        cnt += 1
print(ans, cnt)
