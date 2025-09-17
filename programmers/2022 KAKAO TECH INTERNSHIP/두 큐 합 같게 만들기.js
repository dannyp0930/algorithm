function solution(queue1, queue2) {
    const n = queue1.length;
    let sum1 = queue1.reduce((a, b) => a + b, 0);
    let sum2 = queue2.reduce((a, b) => a + b, 0);
    const half = (sum1 + sum2) / 2;
    const queue = [...queue1, ...queue2];
    let q1 = 0, q2 = n;
    for (let i = 0; i < n * 3; i++) {
        if (sum1 === half) {
            return i;
        }
        if (sum1 > half) {
            sum1 -= queue[q1 % (2 * n)];
            sum2 += queue[q1 % (2 * n)];
            q1++;
        } else {
            sum1 += queue[q2 % (2 * n)];
            sum2 -= queue[q2 % (2 * n)];
            q2++;
        }
    }
    return -1;
}