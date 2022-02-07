from itertools import permutations


def prime(n):
    if n == 0 or n == 1:
        return False
    j = 2
    while j ** 2 <= n:
        if n % j == 0:
            return False
        j += 1
    return True


def solution(numbers):
    answer = 0
    arr = set()
    for i in range(1, len(numbers) + 1):
        for candi in permutations(numbers, i):
            arr.add(int(''.join(candi)))
    for num in arr:
        if prime(num):
            answer += 1
    return answer
