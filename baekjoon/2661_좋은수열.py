def is_good(num):
    N = len(num)
    for i in range(N):
        for j in range(1, N - i):
            if num[i:i + j] == num[i + j:]:
                return False
    return True


def backtrack(num):
    if len(num) == N:
        print(num)
        exit()
    for n in range(1, 4):
        if is_good(num + str(n)):
            backtrack(num + str(n))


N = int(input())
backtrack('')
