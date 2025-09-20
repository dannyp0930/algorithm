function solution(scores) {
    const target = scores[0];
    scores.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]);
    let answer = 1, maxScore = 0;
    const sum = target[0] + target[1];
    scores.forEach((score) => {
       if (score[1] < maxScore) {
           if (score === target) return -1;
       } else {
           maxScore = maxScore < score[1] ? score[1] : maxScore;
           if (score[0] + score[1] > sum) answer++;
       }
    });
    return answer;
}