MAX_NUM = 1000001
N = int(input())
cards = [0] * MAX_NUM
scores = [0] * MAX_NUM
arr = list(map(int, input().split()))
for n in arr:
    cards[n] = 1
for n in arr:
    for i in range(n, MAX_NUM, n):
        if cards[i]:
            scores[n] +=1 
            scores[i] -= 1
print(*[scores[n] for n in arr])
