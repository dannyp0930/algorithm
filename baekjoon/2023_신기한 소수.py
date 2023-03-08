def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def backtrack(num, cnt):
    if cnt == N:
        print(num)
    for i in range(1, 10, 2):
        tmp = 10 * num + i
        if is_prime(tmp):
            backtrack(tmp, cnt + 1)


N = int(input())
prime_list = [2, 3, 5, 7]
for i in range(4):
    backtrack(prime_list[i], 1)
