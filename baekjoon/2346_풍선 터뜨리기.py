from collections import deque


N = int(input())
balloons = deque(enumerate(map(int, input().split())))
ans = []
while balloons:
    idx, balloon = balloons.popleft()
    ans.append(idx + 1)
    if balloon > 0:
        balloons.rotate(-(balloon - 1))
    else:
        balloons.rotate(-balloon)
print(*ans)
