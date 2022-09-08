N = int(input())
A = list(map(int, input().split()))
sorted_A = sorted(A)
P = []
for n in A:
    P.append(sorted_A.index(n))
    sorted_A[sorted_A.index(n)] = -1
print(*P)
