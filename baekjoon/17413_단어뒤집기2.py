S = input()
tag = False
ans = ''
stack = ''
for ch in S:
    if ch == '<':
        tag = True
        ans += stack[::-1]
        stack = ''
        ans += ch
        continue
    elif ch == '>':
        tag = False
        ans += ch
        continue
    elif ch == ' ':
        ans += stack[::-1] + ' '
        stack = ''
        continue
    if tag:
        ans += ch
    else:
        stack += ch
print(ans + stack[::-1])
