const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(input) {
  let t = 0;
  let caseNum = 1;
  while (true) {
    const N = Number(input[t]);
    if (!N) break;
    const graph = input
      .slice(t + 1, t + N + 1)
      .map((x) => x.split(" ").map(Number));
    const dp = Array.from({ length: N }, () => Array(3).fill(Infinity));
    dp[0][1] = graph[0][1];
    dp[0][2] = graph[0][1] + graph[0][2];
    for (let i = 1; i < N; i++) {
      dp[i][0] = graph[i][0] + Math.min(dp[i - 1][0], dp[i - 1][1]);
      dp[i][1] =
        graph[i][1] +
        Math.min(dp[i][0], dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]);
      dp[i][2] = graph[i][2] + Math.min(dp[i][1], dp[i - 1][1], dp[i - 1][2]);
    }
    console.log(`${caseNum}. ${dp[N - 1][1]}`);
    t += N + 1;
    caseNum++;
  }
}

solution(input);
