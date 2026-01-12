const fs = require("fs");
const n = Number(
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim()
);

function solution(n) {
  const N = n > 0 ? n : -n;
  const mod = 1000000000;
  if (n === 0) {
    console.log(0);
    console.log(0);
    return;
  }
  const dp = Array(N + 1).fill(0);
  dp[1] = 1;
  for (let i = 2; i <= N; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod;
  }
  if (n < 0 && !(N % 2)) console.log(-1);
  else console.log(1);
  console.log(dp[N]);
}

solution(n);
