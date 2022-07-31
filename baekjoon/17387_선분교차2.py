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


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
A, B, C, D = point(x1, y1), point(x2, y2), point(x3, y3), point(x4, y4)
L1, L2 = line(A, B), line(C, D)
print(line.cross(L1, L2))