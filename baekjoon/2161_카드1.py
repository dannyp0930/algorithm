N = int(input())
cards = [i for i in range(1, N + 1)]
res = []
while 1:
    res.append(cards.pop(0))
    if not cards:
        break
    cards.append(cards.pop(0))
print(*res)
