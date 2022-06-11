import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()
# 결과값
ans = 0
# 인덱스
i = 0
# IOI반복 횟수
cnt = 0
while i < M - 1:
    if S[i:i + 3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(ans)
