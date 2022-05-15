import sys
sys.stdin = open('1974.txt', 'r')


def sudoku(lst):
    result = 1
    for i in range(9):
        temp1 = set()
        temp2 = set()
        for j in range(9):
            temp1.add(lst[i][j])
            temp2.add(lst[j][i])
        if len(temp1) != 9 or len(temp2) != 9:
            result = 0
            break
    for i in range(0, 7, 3):
        temp = set()
        for j in range(i, i + 3):
            for k in range(i, i + 3):
                temp.add(lst[j][k])
        if len(temp) != 9:
            result = 0
            break
    return result


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print('#{0} {1}'.format(tc, sudoku(arr)))
