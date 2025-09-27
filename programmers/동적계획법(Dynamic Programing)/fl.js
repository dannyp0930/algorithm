function solution(N, number) {
    if (N === number) return 1;
    const dp = Array.from(Array(9), () => new Set());
    for (let i = 1; i < 9; i++) {
        dp[i].add(Number(`${N}`.repeat(i)));
        for (let j = 1; j < i; j++) {
            for (const a of dp[j]) {
                for (const b of dp[i - j]) {
                    dp[i].add(a + b);
                    dp[i].add(a - b);
                    dp[i].add(a * b);
                    dp[i].add(a / b >> 0);
                }
            }
        }
        if (dp[i].has(number)) {
            return i;
        }
    }
    return -1;
}