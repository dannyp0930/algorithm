def solution(N, stages):
    answer = []
    fail = [0] * N
    tot = [0] * N
    percent = [0] * N
    for stage in stages:
        for i in range(stage - 1):
            tot[i] += 1
        if stage <= N:
            tot[stage - 1] += 1
            fail[stage - 1] += 1
    for i in range(N):
        if tot[i]:
            percent[i] = (i + 1, fail[i] / tot[i])
        else:
            percent[i] = (i + 1, 0)
    percent.sort(key=lambda x: -x[1])
    for arr in percent:
        answer.append(arr[0])
    return answer
