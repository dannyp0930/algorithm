def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


N = int(input())
if N == 1:
    N += 1
while 1:
    if is_palindrome(N) and is_prime(N):
        print(N)
        break
    N += 1