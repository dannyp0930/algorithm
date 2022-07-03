import sys


class CircleQueue:
    MAX_SIZE = 100001
    def __init__(self):
        self.rear = 0
        self.front = 0
        self.queue = [0] * self.MAX_SIZE

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.MAX_SIZE == self.front

    def enqueue(self, x):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.MAX_SIZE
            self.queue[self.rear] = x
    
    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.MAX_SIZE
            return self.queue[self.front]


input = sys.stdin.readline
N, K = map(int, input().split())
q = CircleQueue()
q.enqueue(N)
visit = [-1] * 100001
visit[N] = 0
min_sec = 0
cnt = 0
while not q.is_empty():
    x = q.dequeue()
    if x == K:
        cnt += 1
        continue
    for nx in (x - 1, x + 1, 2 * x):
        if nx < 0 or nx > 100000: continue
        if visit[nx] == -1 or visit[nx] == visit[x] + 1:
            visit[nx] = visit[x] + 1
            q.enqueue(nx)
print(visit[K])
print(cnt)
