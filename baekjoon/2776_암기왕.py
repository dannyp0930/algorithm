def binary_search(num):
    s, e = 0, N - 1
    while s <= e:
        m = (s + e) // 2
        if note_1[m] == num:
            return 1
        elif note_1[m] < num:
            s = m + 1
        else:
            e = m - 1
    return 0


for _ in range(int(input())):
    N = int(input())
    note_1 = list(map(int, input().split()))
    note_1.sort()
    M = int(input())
    note_2 = list(map(int, input().split()))
    for num in note_2:
        print(binary_search(num))
