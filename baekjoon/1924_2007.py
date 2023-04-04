month = [
    31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31
]
day = [
    'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'
]

x, y = map(int, input().split())
days = y
for i in range(x - 1):
    days += month[i]
print(day[days % 7])
