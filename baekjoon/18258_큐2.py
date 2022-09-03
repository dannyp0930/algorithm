import sys
input = sys.stdin.readline


N = int(input())
q = [0] * N
front = 0
rear = 0
for _ in range(N):
    command = list(map(str, input().rstrip().split()))
    if command[0] == 'push':
        q[rear] = command[1]
        rear += 1
    elif command[0] == 'pop':
        if front == rear:
            print(-1)
        else:
            print(q[front])
            q[front] = 0
            front += 1
    elif command[0] == 'size':
        print(rear - front)
    elif command[0] == 'empty':
        if front == rear:
            print(1)
        else:
            print(0)
    elif command[0] =='front':
        if front == rear:
            print(-1)
        else:
            print(q[front])
    else:
        if front == rear:
            print(-1)
        else:
            print(q[rear - 1])
