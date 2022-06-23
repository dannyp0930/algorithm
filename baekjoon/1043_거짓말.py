import sys

input = sys.stdin.readline
N, M = map(int, input().split())
truth = set(input().rstrip().split()[1:])
parties = []
ans = M
for _ in range(M):
    party = set(input().rstrip().split()[1:])
    parties.append(party)
for _ in range(M):
    for party in parties:
        if party & truth:
            truth = party | truth
for party in parties:
    if party & truth:
        ans -= 1
print(ans)
