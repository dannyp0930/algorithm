N = int(input())
dic = {}
for _ in range(N):
    book = input()
    if book in dic.keys():
        dic[book] += 1
    else:
        dic[book] = 1
res = list(dic.items())
res.sort(key=lambda x: (-x[1], x[0]))
print(res[0][0])
