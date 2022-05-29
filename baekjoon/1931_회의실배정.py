import sys

input = sys.stdin.readline
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))
ans = 1
end_time = meetings[0][1]
for i in range(1, N):
    if meetings[i][0] >= end_time:
        ans += 1
        end_time = meetings[i][1]
print(ans)
