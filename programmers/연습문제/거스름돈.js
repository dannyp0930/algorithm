function solution(n, money) {
    const mod = 1000000007;
    const dp = Array(n + 1).fill(0);
    dp[0] = 1;
    money.forEach((coin) => {
       for (let i = coin; i <= n; i++) {
           dp[i] = (dp[i] + dp[i - coin]) % mod;
       } 
    });
    return dp[n];
}