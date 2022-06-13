import sys


def command():
    # 뒤집는 횟수 
    cnt = 0
    for p in P:
        # 함수 R
        if p == 'R':
            cnt += 1
        # 함수 D
        # 비어있는 경우
        elif not arr:
            print('error')
            return
        # 현재 뒤집은 횟수가 홀수인 경우
        elif cnt % 2:
            arr.pop()
        # 현재 뒤집은 횟수가 짝수인 경우
        else:
            arr.pop(0)
    # 전체 뒤집은 횟수가 홀수인 경우에만 뒤집는다.
    if cnt % 2:
        arr.reverse()
    print('[' + ','.join(arr) + ']')
    return 


input = sys.stdin.readline
for _ in range(int(input())):
    P = list(map(str, input().rstrip()))
    N = int(input())
    X = input().rstrip()
    arr = list(map(str, X[1:-1].split(','))) if len(X)> 2 else []
    command()
