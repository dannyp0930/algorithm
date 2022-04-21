N = int(input())
now = 0
i = 666
while 1:
    candi = str(i)
    if "666" in candi:
        now += 1
    if now == N:
        print(i)
        break
    i += 1
