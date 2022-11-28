# 카운팅 정렬
import sys

N = int(input())
count = [0] * 10001
for i in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for j in range(10001):
    if count[j]:
        for k in range(count[j]):
            print(j)
