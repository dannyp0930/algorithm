def solution(N):
    q = [i for i in range(10)]
    cnt = -1
    while q:
        n = q.pop(0)
        cnt += 1
        if cnt == N:
            return n
        for i in range(n % 10):
            q.append(n * 10 + i)
    return -1
        
N = int(input())
print(solution(N))