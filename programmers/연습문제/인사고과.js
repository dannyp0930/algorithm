function solution(scores) {
    const target = scores[0];
    scores.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]);
    let answer = 1, before = 0;
    for (const score of scores) {
        if (target[0] < score[0] && target[1] < score[1]) {
            return -1;
        };
        if (before <= score[1]) {
            if (target[0] + target[1] < score[0] + score[1]) {
                answer++;
            }
            before = score[1];
        }
    }
    return answer;
}