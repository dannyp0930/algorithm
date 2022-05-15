while 1:
    n = str(input())
    if n == '0':
        break
    reverse_n = n[::-1]
    if n == reverse_n:
        print('yes')
    else:
        print('no')