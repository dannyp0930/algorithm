S = input()
res = set()
n = len(S)
for i in range(n):
    for j in range(i, n):
        res.add(S[i:j + 1])
print(len(res))