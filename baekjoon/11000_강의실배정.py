from heapq import heappop, heappush


N = int(input())
q = [list(map(int, input().split())) for _ in range(N)]
q.sort()
room = []
heappush(room, q[0][1])
for i in range(1, N):
    if q[i][0] >= room[0]:
        heappop(room)
    heappush(room, q[i][1])
print(len(room))
