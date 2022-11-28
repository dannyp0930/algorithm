import sys

input = sys.stdin.readline
N, M = map(int, input().split())
password_dict = {}
for _ in  range(N):
    address, password = input().split()
    password_dict[address] = password
for _ in range(M):
    print(password_dict[input().rstrip()])