X, Y = map(int, input().split())
Z = 0 if X == 0 else (Y * 100) // X
a = -1 if Z == 99 else (X * (Z + 1) - 100 * Y) / (99 - Z)
if a < 0:
    a = -1
elif a == 0:
    a = 1
elif a > int(a):
    a = int(a) + 1
else:
    a = int(a)
print(a)