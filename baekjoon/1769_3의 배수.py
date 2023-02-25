X = input()
t = 0
while len(X) > 1:
    tmp = 0
    for n in X:
        tmp += int(n)
    X = str(tmp)
    t += 1
print(t)
print('YES' if int(X) % 3 == 0 else 'NO')
