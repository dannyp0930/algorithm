function solution(s) {
    let answer = 1;
    const n = s.length;
    const dp = Array.from(Array(n), () => Array(n).fill(false));
    for (let i = 0; i < n; i++) {
        dp[i][i] = true;
    }
    for (let i = 0; i < n - 1; i++) {
        if (s[i] === s[i + 1]) {
            answer = 2;
            dp[i][i + 1] = true;
        }
    }
    for (let i = 3; i <= n; i++) {
        for (let l = 0; l <= n - i; l++) {
            const r = l + i - 1;
            if (s[l] === s[r] && dp[l + 1][r - 1]) {
                dp[l][r] = true;
                answer = answer < i ? i : answer;
            }
        }
    }
    return answer;
}