cnt_divisor = int(input())
divisors = list(map(int, input().split()))
if cnt_divisor == 1:
    N = divisors[0] ** 2
else:
    divisors.sort()
    N = divisors[0] * divisors[-1]
print(N)
