N, K, I = map(int, input().split())
K -= 1
I -= 1
round = 1
while 1:
    if K // 2 == I // 2:
        break
    round += 1
    K //= 2
    I //= 2
print(round)
