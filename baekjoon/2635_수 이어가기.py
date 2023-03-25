n = int(input())
length = 0
res = []
for i in range(n + 1):
    tmp = [n, i]
    j = 0
    while 1:
        m = tmp[j] - tmp[j + 1]
        if m < 0:
            break
        tmp.append(m)
        j += 1
    if length < len(tmp):
        length = len(tmp)
        res = tmp
print(length)
print(*res)
