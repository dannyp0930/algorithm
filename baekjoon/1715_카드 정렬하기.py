from heapq import heappop, heappush
import sys


input = sys.stdin.readline
N = int(input())
cards = []
for _ in range(N):
    heappush(cards, int(input()))
if len(cards) == 1:
    print(0)
else:
    res = 0
    while len(cards) > 1:
        comb = heappop(cards) + heappop(cards)
        res += comb
        heappush(cards, comb)
    print(res)