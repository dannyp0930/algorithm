N = int(input())
M = -N
cnt = 0
for _ in range(32):
    if M & 1 != N & 1:
        cnt += 1
    M >>= 1
    N >>= 1
print(cnt)