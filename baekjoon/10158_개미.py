w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
a, b = (p + t) // w, (q + t) // h
x, y = (p + t) % w, (q + t) % h
print(w - x if a % 2 else x, h - y if b % 2 else y)
