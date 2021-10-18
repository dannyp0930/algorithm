# 백트래킹

def comb(cnt):
    if len(stack) == 6:
        print(*stack)
        return
    for i in range(cnt, K + 1):
        stack.append(arr[i])
        comb(i + 1)
        stack.pop()


while 1:
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        break
    K = arr[0]
    stack = []
    comb(1)
    print()
