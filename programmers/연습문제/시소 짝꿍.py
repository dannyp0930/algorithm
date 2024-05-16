from collections import Counter


def solution(weights):
    ans = 0
    counter = Counter(weights)
    for i in range(100, 1001):
        if counter[i]:
            ans += counter[i] * (counter[i] - 1) // 2
            ans += counter[i] * counter[i * 2]
            ans += counter[i] * counter[i * 3 / 2]
            ans += counter[i] * counter[i * 4 / 3]
    return ans
