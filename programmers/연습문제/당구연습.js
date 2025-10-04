function solution(m, n, startX, startY, balls) {
    const answer = [];
    balls.forEach(([endX, endY]) => {
        const candi = [];
        if (startX !== endX || startY < endY) candi.push((startX - endX) ** 2 + (startY + endY) ** 2);
        if (startX !== endX || startY > endY) candi.push((startX - endX) ** 2 + (2 * n - startY - endY) ** 2);
        if (startY !== endY || startX < endX) candi.push((startX + endX) ** 2 + (startY - endY) ** 2);
        if (startY !== endY || startX > endX) candi.push((2 * m - startX - endX) ** 2 + (startY - endY) ** 2);
        answer.push(Math.min(...candi));
    });
    return answer;
}
