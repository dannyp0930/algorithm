import sys

input = sys.stdin.readline

M = int(input())
SET = set()
for _ in range(M):
    command = input().split()
    if len(command) > 1:
        command[1] = int(command[1])
    if command[0] == 'add':
        SET.add(command[1])
    elif command[0] == 'remove':
        SET.discard(command[1])
    elif command[0] == 'check':
        if command[1] in SET:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if command[1] in SET:
            SET.remove(command[1])
        else:
            SET.add(command[1])
    elif command[0] == 'all':
        SET = set([i for i in range(1, 21)])
    else:
        SET = set()
