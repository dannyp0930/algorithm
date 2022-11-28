def is_empty():
    if front == rear:
        return True
    return False


def insert(num):
    global rear
    q[rear] = num
    rear += 1


def delete():
    global front
    res = q[front]
    q[front] = 0
    front += 1
    return res

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1
front = rear = 0
q = [0] * N
for i in range(1, N + 1):
    if not in_degree[i]:
        insert(i)
res = []
while not is_empty():
    u = delete()
    res.append(u)
    for v in graph[u]:
        in_degree[v] -= 1
        if not in_degree[v]:
            insert(v)
print(*res)
