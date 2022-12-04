import sys

input = sys.stdin.readline
stack1 = list(input().rstrip())
stack2 = []
M = int(input())
for _ in range(M):
    command = list(input().split())
    if command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif command[0] == 'B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(command[1])
print(''.join(stack1 + stack2[::-1]))
