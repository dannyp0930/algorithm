N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
for n in arr:
    print(n)
