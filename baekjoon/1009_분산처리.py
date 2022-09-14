for _ in range(int(input())):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [4, 9]:
        if b % 2 == 1:
            print(a)
        else:
            print(a * a % 10)
    else:
        b %= 4
        if b == 0:
            print(a ** 4 % 10)
        else:
            print(a ** b % 10)