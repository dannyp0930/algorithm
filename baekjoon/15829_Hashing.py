L = int(input())
string = input()
ans = 0
for i, ch in enumerate(string):
    num = ord(ch) - 96
    ans += (num * 31 ** i)
print(ans % 1234567891)
