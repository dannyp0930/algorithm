for _ in range(int(input())):
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    print(N - 1)