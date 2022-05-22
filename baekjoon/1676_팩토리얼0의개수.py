N = int(input())
cnt = 0
while N > 1:
    if not N % 125:
        cnt += 3
    elif not N % 25:
        cnt += 2
    elif not N % 5:
        cnt += 1
    N -= 1
print(cnt)
