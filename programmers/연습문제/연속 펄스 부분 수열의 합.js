function solution(sequence) {
    let ans = 0;
    const n = sequence.length;
    const plus = Array(n).fill(0);
    const minus = Array(n).fill(0);
    sequence.forEach((seq, i) => {
        if (i === 0) {
            plus[i] = seq;
            minus[i] = -seq;
        } else if (i % 2) {
            plus[i] = Math.max(plus[i - 1] - seq, -seq);
            minus[i] = Math.max(minus[i - 1] + seq, seq);
        } else {
            plus[i] = Math.max(plus[i - 1] + seq, seq);
            minus[i] = Math.max(minus[i - 1] - seq, -seq);
        }
        ans = Math.max(ans, plus[i], minus[i]);
    });
    return ans;
}