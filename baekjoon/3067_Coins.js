const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const T = Number(input[0]);
const test = input.slice(1);

function solution(T, test) {
  const solve = (coins, M) => {
    const dp = Array(M + 1).fill(0);
    dp[0] = 1;
    for (const coin of coins) {
      for (let i = coin; i <= M; i++) {
        dp[i] += dp[i - coin];
      }
    }
    return dp[M];
  };
  let idx = 0;
  while (T--) {
    const N = Number(test[idx++]);
    const coins = test[idx++].split(" ").map(Number);
    const M = Number(test[idx++]);
    console.log(solve(coins, M));
  }
}

solution(T, test);
