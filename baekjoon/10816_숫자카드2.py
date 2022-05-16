N = int(input())
cards = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
cards_dic = dict()
for card in cards:
    if card in cards_dic:
        cards_dic[card] += 1
    else:
        cards_dic[card] = 1
result = []
for num in arr:
    if num in cards_dic:
        result.append(cards_dic[num])
    else:
        result.append(0)
print(*result)