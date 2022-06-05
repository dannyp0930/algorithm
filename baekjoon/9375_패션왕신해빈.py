import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    closet = dict()
    for _ in range(n):
        name, category = input().split()
        if category in closet.keys():
            closet[category] += 1
        else:
            closet[category] = 1
    ans = 1
    for v in closet.values():
        ans *= (v + 1)
    print(ans - 1)
