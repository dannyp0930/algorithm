const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const street = input[1];

function solution(N, street) {
  const dp = Array(N).fill(Infinity);
  dp[0] = 0;
  const order = {
    B: "J",
    O: "B",
    J: "O",
  };
  for (let i = 1; i < N; i++) {
    const b = order[street[i]];
    for (let j = i - 1; j >= 0; j--) {
      if (b === street[j]) {
        dp[i] = Math.min(dp[i], dp[j] + (j - i) * (j - i));
      }
    }
  }
  console.log(dp[N - 1] === Infinity ? -1 : dp[N - 1]);
}

solution(N, street);
