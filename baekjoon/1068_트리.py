N = int(input())
parent = list(map(int, input().split()))
q = [int(input())]
while q:
    n = q.pop(0)
    for i, p in enumerate(parent):
        if p == n:
            q.append(i)
    parent[n] = -2
cnt = 0
for n in range(N):
    if parent[n] != -2 and n not in parent:
        cnt += 1
print(cnt)