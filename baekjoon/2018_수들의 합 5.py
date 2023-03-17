N = int(input())
s = e = cnt = tot = 0
while e <= N:
    if tot < N:
        e += 1
        tot += e
    elif tot > N:
        tot -= s
        s += 1
    else:
        cnt += 1
        e += 1
        tot += e
print(cnt)
