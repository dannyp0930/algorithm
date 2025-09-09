function solution(n) {
    if (n % 2) return 0;
    const dp = [0, 3, 11];
    const mod = 1000000007;
    const index = Math.ceil(n / 2);
    for (let i = 3; i <= index; i++) {
        dp.push((mod + 4 * dp[i - 1] - dp[i - 2]) % mod);
    }
    return dp[index];
}