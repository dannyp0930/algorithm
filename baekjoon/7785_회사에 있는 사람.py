n = int(input())
office = {}
for _ in range(n):
    record = list(input().split())
    if record[1] == 'enter':
        office[record[0]] = 1
    elif record[1] == 'leave':
        office[record[0]] = 0
res = []
for k, v in office.items():
    if v:
        res.append(k)
res.sort(reverse=True)
for n in res:
    print(n)
