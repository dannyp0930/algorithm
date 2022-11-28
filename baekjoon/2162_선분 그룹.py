import sys
input = sys.stdin.readline


class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def ccw(self, other1, other2):
        ans = (other1.x - self.x) * (other2.y - self.y) - (other1.y - self.y) * (other2.x - self.x)
        if ans < 0:
            return -1
        elif ans > 0:
            return 1
        return 0

    def __le__(self, other):
        if self.x == other.x:
            return self.y <= other.y
        return self.x <= other.x


class line():
    def __init__(self, p1, p2):
        if p1 <= p2:
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1

    def cross(self, other):
        ccw1 = point.ccw(self.p1, self.p2, other.p1) * point.ccw(self.p1, self.p2, other.p2)
        ccw2 = point.ccw(other.p1, other.p2, self.p1) * point.ccw(other.p1, other.p2, self.p2)
        if ccw1 == 0 and ccw2 == 0:
            if self.p1 <= other.p2 and other.p1 <= self.p2:
                return 1
        elif ccw1 <= 0 and ccw2 <= 0:
            return 1
        return 0


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N)]
for i in range(N):
    x1, y1, x2, y2 = lines[i]
    p1, p2 = point(x1, y1), point(x2, y2)
    l1 = line(p1, p2)
    for j in range(i):
        x3, y3, x4, y4 = lines[j]
        p3, p4 = point(x3, y3), point(x4, y4)
        l2 = line(p3, p4)
        if line.cross(l1, l2):
            union(i ,j)
cnt = 0
group_cnt = [0] * N
for i in range(N):
    if i == parent[i]:
        cnt += 1
    group_cnt[find(i)] += 1
print(cnt)
print(max(group_cnt))