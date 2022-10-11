N, K = map(int, input().split())
schedule = list(map(int, input().split()))
plugged = [0] * (K + 1)
cnt = 0
ans = 0
for i, s in enumerate(schedule):
    if not plugged[s]:
        if cnt < N:
            plugged[s] = 1
            cnt += 1
        else:
            unplug = 0
            tmp = schedule[i:]
            for p in range(1, K + 1):
                if plugged[p] and p not in tmp:
                    unplug = p
                    break
            if not unplug:
                visit = [0] * (K + 1)
                used_cnt = 0
                for p in tmp:
                    if not visit[p] and plugged[p]:
                        visit[p] = 1
                        used_cnt += 1
                    if used_cnt == N:
                        unplug = p
                        break
            plugged[unplug] = 0
            plugged[s] = 1
            ans += 1
print(ans)
