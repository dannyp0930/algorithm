def blackjack(idx, cnt):
    global tmp, result
    if tmp > M:
        return
    if cnt == 3:
        if result < tmp:
            result = tmp
        return
    for i in range(idx, N):
        tmp += cards[i]
        blackjack(i + 1, cnt + 1)
        tmp -= cards[i]


N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0
tmp = 0
blackjack(0, 0)
print(result)
