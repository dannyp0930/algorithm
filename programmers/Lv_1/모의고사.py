def solution(answers):
    answer = []
    cnt = len(answers)
    score = [0, 0, 0]
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3]
    ]
    for i in range(cnt):
        if answers[i] == pattern[0][i % 5]:
            score[0] += 1
        if answers[i] == pattern[1][i % 8]:
            score[1] += 1
        if answers[i] == pattern[2][i % 10]:
            score[2] += 1
    max_score = max(score)
    for j in range(3):
        if score[j] == max_score:
            answer.append(j + 1)
    return answer
