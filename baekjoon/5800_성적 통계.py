for i in range(int(input())):
    arr = list(map(int, input().split()))
    N, grades = arr[0], sorted(arr[1:])
    max_grade = grades[-1]
    min_grade = grades[0]
    largest_gap = max([grades[j + 1] - grades[j] for j in range(N - 1)])
    print(f"Class {i + 1}")
    print(f"Max {max_grade}, Min {min_grade}, Largest gap {largest_gap}")
