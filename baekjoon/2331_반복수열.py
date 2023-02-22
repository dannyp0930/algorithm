def repeat(num):
    x = 0
    while num:
        x += (num % 10) ** P
        num //= 10
    return x


A, P = map(int, input().split())
D = [A]
num = A
while 1:
    num = repeat(num)
    if num in D:
        print(D.index(num))
        break
    D.append(num)
