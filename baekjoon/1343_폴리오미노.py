arr = list(input().split('.'))
flag = True
for i in range(len(arr)):
    length = len(arr[i])
    if not length:
        continue
    q = length // 4
    r = length % 4
    if r == 0:
        arr[i] = 'AAAA' * q
    elif r == 2:
        arr[i] = 'AAAA' * q + 'BB'
    else:
        flag = False
        break
if flag:
    print('.'.join(arr))
else:
    print(-1)
