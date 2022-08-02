import sys
input = sys.stdin.readline


def get_left(i, total):
    if i == N // 2:
        A.append(total)
        return
    get_left(i + 1, total + arr[i])
    get_left(i + 1, total)


def get_right(i, total):
    if i == N:
        B.append(total)
        return
    get_right(i + 1, total + arr[i])
    get_right(i + 1, total)
        

N, S = map(int, input().split())
arr = list(map(int, input().split()))
A = []
B = []
get_left(0, 0)
get_right(N // 2, 0)
A.sort()
B.sort(reverse=True)
ans = 0
a, b = 0, 0
while a < len(A) and b < len(B):
    total = A[a] + B[b]
    if total == S:
        cnt_a = 0
        target_a = A[a]
        while a < len(A) and A[a] == target_a:
            a += 1
            cnt_a += 1
        cnt_b = 0
        target_b = B[b]
        while b < len(B) and B[b] == target_b:
            b += 1
            cnt_b += 1
        ans += cnt_a * cnt_b
    elif total < S:
        a += 1
    else:
        b += 1
if not S: ans -= 1
print(ans)
