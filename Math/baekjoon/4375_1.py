while 1:
    try:
        n = int(input())
    except:
        break
    i = 1
    while 1:
        num = int('1' * i)
        if not num % n:
            print(i)
            break
        i += 1
