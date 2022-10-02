def is_leap(y):
    if y % 4 != 0: return False
    if y % 100 != 0: return True
    if y % 400 == 0: return True
    return False


def get_days(y, m, d):
    res = 0
    for i in range(y):
        res += 365 + is_leap(i)
    for j in range(m - 1):
        if j == 1: res += is_leap(y)
        res += month[j]
    return res + d


month = [
    31, 28, 31, 30,
    31, 30, 31, 31,
    30, 31, 30, 31
]
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
today = get_days(y1, m1, d1)
d_day = get_days(y2, m2, d2)
after_1000 = get_days(y1 + 1000, m1, d1)
if after_1000 <= d_day:
    print('gg')
else:
    print('D-{0}'.format(d_day - today))