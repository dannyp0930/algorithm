N, L = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
for i in range(N):
    if L >= h[i]:
        L += 1
    else:
        break
print(L)
