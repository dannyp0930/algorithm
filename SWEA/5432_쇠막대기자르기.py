import sys
sys.stdin = open('5432.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    string = input()
    N = len(string)
    stack = []
    cnt = 0
    for i in range(N):
        if string[i] == '(':
            stack.append(string[i])
        else:
            stack.pop()
            if string[i - 1] == '(':
                cnt += len(stack)
            else:
                cnt += 1
    print('#{0} {1}'.format(tc, cnt))