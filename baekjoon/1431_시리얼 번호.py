def sum_num(sn):
    res = 0
    for ch in sn:
        try:
            res += int(ch)
        except:
            continue
    return res


N = int(input())
arr = [input() for _ in range(N)]
arr.sort(key=lambda x: (len(x), sum_num(x), x))
for sn in arr:
    print(sn)
