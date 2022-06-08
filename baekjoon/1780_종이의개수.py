import sys


# 자른 종이가 같은 숫자인지 판별
def same(r, c, n):
    first = paper[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[i][j] != first:
                return False
    return True


# 종이별 숫자 세기
def count(r, c, n):
    global cnt_minus, cnt_zero, cnt_plus

    # 모두 같은 숫자이면 종이 세기
    if same(r, c, n):
        num = paper[r][c]
        if num == -1:
            cnt_minus += 1
        elif num == 1:
            cnt_plus += 1
        else:
            cnt_zero += 1
        return
    
    # 9부분으로 나누기
    for i in range(3):
        for j in range(3):
            count(r + n // 3 * i, c + n // 3 * j, n // 3)

input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt_minus = cnt_zero = cnt_plus = 0
count(0, 0, N)
print(cnt_minus)
print(cnt_zero)
print(cnt_plus)
