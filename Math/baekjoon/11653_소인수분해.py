N = int(input())
m = 2
while N != 1:
    if not N % m:
        print(m)
        N //= m
    else:
        m += 1
