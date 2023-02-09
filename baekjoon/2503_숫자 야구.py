from itertools import permutations


num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
candi = list(permutations(num, 3))
N = int(input())
for _ in range(N):
    q, s, b = map(int, input().split())
    q = list(str(q))
    cnt = 0
    for i in range(len(candi)):
        strike = ball = 0
        i -= cnt
        for j in range(3):
            if candi[i][j] == q[j]:
                strike += 1
            elif q[j] in candi[i]:
                ball += 1
        if strike != s or ball != b:
            candi.remove(candi[i])
            cnt += 1
print(len(candi))
