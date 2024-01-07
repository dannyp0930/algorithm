from itertools import permutations
import sys
input = sys.stdin.readline


def get_score(order):
    idx = 0
    score = 0
    for inning in arr:
        cnt = 0
        b1 = b2 = b3 = 0
        while cnt < 3:
            if inning[order[idx]] == 0:
                cnt += 1
            elif inning[order[idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[order[idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif inning[order[idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            else:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0
            idx = (idx + 1) % 9
    return score


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for order in permutations(range(1, 9), 8):
    order = list(order[:3]) + [0] + list(order[3:])
    ans = max(ans, get_score(order))
print(ans)
    