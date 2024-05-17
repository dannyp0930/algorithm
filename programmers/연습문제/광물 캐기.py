from functools import reduce


def solution(picks, minerals):

    ans = 0
    fatigue = []
    score = {"diamond": 25, "iron": 5, "stone": 1}
    n = len(minerals)
    for i in range(0, n, 5):
        arr = minerals[i:i + 5] if i + 5 < n else minerals[i::]
        tmp = reduce(lambda acc, cur: acc + score[cur], arr, 0)
        fatigue.append((tmp, arr))
    if len(fatigue) > sum(picks):
        fatigue = fatigue[:sum(picks)]
    fatigue.sort(key=lambda x: -x[0])
    for f in fatigue:
        if picks[0]:
            picks[0] -= 1
            ans += len(f[1])
        elif picks[1]:
            picks[1] -= 1
            ans += sum(5 if s == "diamond" else 1 for s in f[1])
        elif picks[2]:
            picks[2] -= 1
            ans += sum(score[s] for s in f[1])
        else:
            break
    return ans
