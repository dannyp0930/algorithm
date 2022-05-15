while 1:
    a, b, c = map(int, input().split())
    if not a:
        break
    ans = False
    l = max(a, b, c)
    s1, s2 = (i for i in (a, b, c) if i != l)
    if l ** 2 == s1 ** 2 + s2 ** 2:
        ans = True
    if ans:
        print('right')
    else:
        print('wrong')
