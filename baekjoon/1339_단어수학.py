N = int(input())
words = [input() for _ in range(N)]
dic = {}
for word in words:
    length = len(word) - 1
    for i, c in enumerate(word):
        if c in dic:
            dic[c] += 10 ** (length - i)
        else:
            dic[c] = 10 ** (length - i)
arr = sorted(dic.values(), reverse=True)
res, num = 0, 9
for v in arr:
    res += v * num
    num -= 1
print(res)
