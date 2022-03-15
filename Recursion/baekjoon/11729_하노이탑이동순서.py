def hanoi(num, from_, to_, via_):
    if num == 1:
        print(from_, to_)
    else:
        hanoi(num - 1, from_, via_, to_)
        print(from_, to_)
        hanoi(num - 1, via_, to_, from_)


N = int(input())
K = 2 ** N - 1
print(K)
hanoi(N, 1, 3, 2)
