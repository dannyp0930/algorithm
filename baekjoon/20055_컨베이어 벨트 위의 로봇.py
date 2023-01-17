from collections import deque


N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * N)
t = 0
while 1:
    t += 1
    belt.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0
    for i in range(N - 2, -1, -1):
        if robot[i] and belt[i + 1] and not robot[i + 1]:
            robot[i + 1] = 1
            robot[i] = 0
            belt[i + 1] -= 1
    robot[-1] = 0
    if belt[0] and not robot[0]:
        robot[0] = 1
        belt[0] -= 1
    if belt.count(0) >= K:
        break
print(t)
