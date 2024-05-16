def solution(targets):
    ans = 1
    targets.sort(key=lambda x: (x[0], -x[1]))
    s, e = 0, 100000000
    for ts, te in targets:
        if s <= ts and te <= e:
            s, e = ts, te
        elif ts < e <= te:
            s = ts
        elif e <= ts:
            s, e = ts, te
            ans += 1
    return ans
