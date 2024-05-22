def solution(topping):
    ans = 0
    old = {}
    young = {}
    for t in topping:
        if t in old.keys():
            old[t] += 1
        else:
            old[t] = 1
    for t in topping:
        old[t] -= 1
        if not old[t]:
            del old[t]
        if t in young.keys():
            young[t] += 1
        else:
            young[t] = 1
        if len(old) == len(young):
            ans += 1
    return ans
