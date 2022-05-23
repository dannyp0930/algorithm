import sys

input = sys.stdin.readline

N, M = map(int, input().split())
no_hear = set([input().rstrip() for _ in range(N)])
no_see = set([input().rstrip() for _ in range(M)])
intersect = sorted(list(no_hear & no_see))
print(len(intersect))
for name in intersect:
    print(name)