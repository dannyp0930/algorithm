string = input()
bomb = input()
bomb_size = len(bomb)
stack = []
for ch in string:
    stack.append(ch)
    if ''.join(stack[-bomb_size:]) == bomb:
        for _ in range(bomb_size):
            stack.pop()
if not stack:
    print('FRULA')
else:
    print(''.join(stack))
