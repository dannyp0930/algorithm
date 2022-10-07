def solution(begin, target, words):
    n = len(words)
    q = [[begin, 0]]
    visit = [0] * n
    while q:
        word, cnt = q.pop(0)
        if word == target:
            return cnt
        for i in range(n):
            if not visit[i]:
                diff_cnt = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff_cnt += 1
                    if diff_cnt > 1:
                        break
                if diff_cnt == 1:
                    q.append([words[i], cnt + 1])
                    visit[i] = 1
    return 0
