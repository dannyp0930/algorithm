def solution(a, b):
    visit = [0] * 10000
    q = [(a, 0)]
    visit[a] = 1
    while q:
        num, cnt = q.pop(0)
        if num == b:
            return cnt
        for i in range(4):
            digit = (num // 10 ** i) % 10
            for j in range(10):
                if i == 3 and j == 0:
                    continue
                if digit == j:
                    continue
                new_num = num + (j - digit) * (10 ** i)
                if not visit[new_num] and prime_list[new_num]:
                    q.append((new_num, cnt + 1))
                    visit[new_num] = 1
    return 'Impossible'


prime_list = [1] * 10000
for i in range(2, 101):
    if prime_list[i]:
        for j in range(i + i, 10000, i):
            prime_list[j] = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(solution(a, b))
