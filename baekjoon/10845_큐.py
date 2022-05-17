import sys

q = []
for _ in range(int(sys.stdin.readline())):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'push':
        q.append(int(command[1]))
    elif command[0] == 'pop':
        try:
            print(q.pop(0))
        except:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        try:
            print(q[0])
        except:
            print(-1)
    else:
        try:
            print(q[-1])
        except:
            print(-1)
