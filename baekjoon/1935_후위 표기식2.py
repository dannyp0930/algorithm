N = int(input())
exp = list(input())
num = {chr(i): int(input()) for i in range(65, 65 + N)}
stack = []
for ch in exp:
    try:
        stack.append(num[ch])
    except:
        res = 0
        a, b = stack.pop(), stack.pop()
        if ch == '+':
            res = a + b
        elif ch == '-':
            res = b - a
        elif ch == '*':
            res = a * b
        else:
            res = b / a
        stack.append(res)
ans = stack[0]
print("{:.2f}".format(ans))
