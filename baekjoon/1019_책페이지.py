def calc(n):
    while n:
        page[n % 10] += cnt
        n //= 10

S = 1
N = int(input())
cnt = 1
page = [0] * 10
while S <= N:
    while N % 10 != 9:
        calc(N)
        N -= 1
    if S > N:
        break
    while S % 10 != 0:
        calc(S)
        S += 1
    S //= 10
    N //= 10
    for i in range(10):
        page[i] += (N - S + 1) * cnt
    cnt *= 10
print(*page)
