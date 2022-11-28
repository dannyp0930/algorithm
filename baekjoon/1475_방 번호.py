N = int(input())
num = [0] * 10
while N:
    n = N % 10
    if n == 6 or n == 9:
        if num[6] < num[9]:
            num[6] += 1
        else:
            num[9] += 1
    else:
        num[n] += 1
    N //= 10
print(max(num))
