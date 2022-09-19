import re


pattern = '(100+1+|01)+'
regex = re.compile(pattern)
for _ in range(int(input())):
    sign = input()
    match = regex.fullmatch(sign)
    if match:
        print('YES')
    else:
        print('NO')
