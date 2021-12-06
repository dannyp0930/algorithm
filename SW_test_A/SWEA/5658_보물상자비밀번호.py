import sys
sys.stdin = open('5658.txt', 'r')

for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    hex_num = list(input())
    rotate = N // 4
    num_list = set()
    for i in range(rotate):
        for j in range(4):
            string = ''.join(hex_num[rotate * j: rotate * (j + 1)])
            num_list.add(int(string, 16))
        tmp = hex_num.pop()
        hex_num.insert(0, tmp)
    ans = sorted(num_list, reverse=True)
    print('#{} {}'.format(T, ans[K - 1]))
