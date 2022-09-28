N = int(input())
crain = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
box = sorted(list(map(int, input().split())), reverse=True)
if crain[0] < box[0]:
    print(-1)
else:
    c_pos = [0] * N
    visit = [0] * M
    res = 0
    cnt = 0
    while cnt < M:
        res += 1
        for c in range(N):
            while c_pos[c] < M:
                if not visit[c_pos[c]] and box[c_pos[c]] <= crain[c]:
                    visit[c_pos[c]] = 1
                    c_pos[c] += 1
                    cnt += 1
                    break
                c_pos[c] += 1    
    print(res)
