function solution(target) {
    const dp = Array.from(Array(target + 1), () => [Infinity, 0]);
    dp[0] = [0, 0];
    for (let n = 1; n <= target; n++) {
        for (let i = 1; i <= 20; i++) {
            if (n < i) break;
            const [curDart, curCnt] = dp[n];
            const [nextDart, nextCnt] = [dp[n - i][0] + 1, dp[n - i][1] + 1];
            if (nextDart < curDart || (nextDart === curDart && curCnt < nextCnt)) {
                dp[n] = [nextDart, nextCnt];
            }
        }
        for (let i = 1; i <= 20; i++) {
            if (n < i * 2) break;
            const [curDart, curCnt] = dp[n];
            const [nextDart, nextCnt] = [dp[n - i * 2][0] + 1, dp[n - i * 2][1]];
            if (nextDart < curDart || (nextDart === curDart && curCnt < nextCnt)) {
                dp[n] = [nextDart, nextCnt];
            }
        }
        for (let i = 1; i <= 20; i++) {
            if (n < i * 3) break;
            const [curDart, curCnt] = dp[n];
            const [nextDart, nextCnt] = [dp[n - i * 3][0] + 1, dp[n - i * 3][1]];
            if (nextDart < curDart || (nextDart === curDart && curCnt < nextCnt)) {
                dp[n] = [nextDart, nextCnt];
            }
        }
        if (n >= 50) {
            const [curDart, curCnt] = dp[n];
            const [nextDart, nextCnt] = [dp[n - 50][0] + 1, dp[n - 50][1] + 1];
            if (nextDart < curDart || (nextDart === curDart && curCnt < nextCnt)) {
                dp[n] = [nextDart, nextCnt];
            }
        }
    }
    return dp[target];
}