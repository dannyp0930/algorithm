S = input()
res = []
for i in range(len(S)):
    res.append(S[i:])
res.sort()
for s in res:
    print(s)
    