import sys
sys.stdin = open('2383.txt', 'r')


def calc(lst, stair):
    cnt = d_cnt = 0
    q = []
    while lst or q or d_cnt:
        # 대기 인원이 있다면
        while d_cnt:
            # 3명이 찼다면 정지
            if len(q) == 3:
                break
            # 내려가는 사람들 q에 계단 내려가는 시간 입력
            q.append(stair[2])
            # 대기 인원 감소
            d_cnt -= 1

        # 내려가는 인원만큼 동작
        for d in range(len(q) - 1, -1, -1):
            # 시간 감소
            q[d] -= 1
            # 다 내려갔다면 제거
            if q[d] <= 0:
                q.pop(d)
        # 이동중인 인원만큼 동작
        for m in range(len(lst) - 1, -1, -1):
            # 거리 감소
            lst[m] -= 1
            # 계단 도착하면
            if lst[m] <= 0:
                # 이동 중 인원 제거 및 대기 인원 증가
                lst.pop(m)
                d_cnt += 1
        cnt += 1
    return cnt


def dfs(idx):
    global ans
    if idx == num:
        stairs1, stairs2 = [], []
        for n in range(num):
            if check[n]:
                stairs1.append(people[n][0])
            else:
                stairs2.append(people[n][1])
        cnt = max(calc(sorted(stairs1), stairs[0]), calc(sorted(stairs2), stairs[1]))
        ans = min(cnt, ans)
        return
    check[idx] = 0
    dfs(idx + 1)
    check[idx] = 1
    dfs(idx + 1)


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people, stairs = [], []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people.append([i, j])
            elif arr[i][j] > 1:
                stairs.append((i, j, arr[i][j]))
    num = len(people)
    for k in range(num):
        d1 = abs(people[k][0] - stairs[0][0]) + abs(people[k][1] - stairs[0][1])
        d2 = abs(people[k][0] - stairs[1][0]) + abs(people[k][1] - stairs[1][1])
        people[k][0], people[k][1] = d1, d2
    check = [0] * num
    ans = 0xffffff
    dfs(0)
    print('#{} {}'.format(T, ans + 1))

