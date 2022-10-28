def solution(n, stations, w):
    ans = 0
    l = len(stations)
    idx = 0
    now = 1
    while now <= n:
        if idx < l and now >= stations[idx] - w:
            now = stations[idx] + w + 1
            idx += 1
        else:
            now += 2 * w + 1
            ans += 1
    return ans