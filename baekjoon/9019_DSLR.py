from collections import deque
import sys

def command(N, C):
    if C == 'D':
        return (N * 2) % 10000
    if C == 'S':
        return N - 1 if N else 9999
    if C == 'L':
        return (N % 1000) * 10 + (N // 1000)
    if C == 'R':
        return (N % 10) * 1000 + N // 10


def DSLR():
   while queue:
        n, c = queue.popleft()
        if n == B:
            print(c)
            return
        for C in ['D', 'S', 'L', 'R']:
            new_n = command(n, C)
            new_c = c + C
            if not visit[new_n]:
                queue.append((new_n, new_c))
                visit[new_n] = 1
            

input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    queue = deque([(A, '')])
    visit = [0] * 10000
    visit[A] = 1
    DSLR()
