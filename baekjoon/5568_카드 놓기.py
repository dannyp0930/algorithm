from itertools import permutations


n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
res = set()
for arr in permutations(cards, k):
    res.add(''.join(arr))
print(len(res))
