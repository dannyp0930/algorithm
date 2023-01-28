A, B = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))
num = 0
for n in arr:
    num += n * A ** (m - 1)
    m -= 1
ans = []
while num:
    ans.append(num % B)
    num //= B
print(*ans[::-1])
