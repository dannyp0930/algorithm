import sys
sys.stdin = open('2328.txt', 'r')

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

for T in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    # 가로, 세로, 미생물 수, 방향
    arr = [list(map(int, input().split())) for _ in range(K)]
    for _ in range(M):
        # 값을 꺼낼때 마다 기록
        cnt = -1
        # 방문 기록, 총 미생물, 최대 값, cnt
        visit = [[0] * N for _ in range(N)]
        for m in arr:
            cnt += 1
            if m[2]:
                # 약물 위치로 갈 경우
                nr, nc = m[0] + dr[m[3]], m[1] + dc[m[3]]
                if nr == 0 or nc == 0 or nr == N - 1 or nc == N - 1:
                    m[2] //= 2
                    if m[3] == 1 or m[3] == 3:
                        m[3] += 1
                    else:
                        m[3] -= 1
                else:
                    # 이동할 곳이 비어있는 경우
                    if not visit[nr][nc]:
                        visit[nr][nc] = [m[2], m[2], cnt]
                    else:
                        # 현재까지 미생물 수 합하기
                        visit[nr][nc][0] += m[2]
                        # 기존의 최댓값이 추가하려는 값보다 큰 경우
                        if visit[nr][nc][1] > m[2]:
                            # 저장된 미생물 값에도 추가
                            arr[visit[nr][nc][2]][2] = visit[nr][nc][0]
                            # 현재 저장된 미생물 0으로
                            m[2] = 0
                        else:
                            # 최댓값 변경
                            visit[nr][nc][1] = m[2]
                            # 미생물 값 0으로
                            arr[visit[nr][nc][2]][2] = 0
                            # cnt 변경
                            visit[nr][nc][2] = cnt
                            # 미생물 값 변경
                            m[2] = visit[nr][nc][0]
                m[0], m[1] = nr, nc
    ans = 0
    for lst in arr:
        ans += lst[2]
    print('#{} {}'.format(T, ans))

