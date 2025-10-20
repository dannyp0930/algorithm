const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const S = input[1].split(" ").map(Number);

function solution(N, S) {
  const maxSum = S.reduce((a, c) => a + c);
  const sumArr = Array(maxSum + 2).fill(0);
  const dfs = (i, sum) => {
    if (i === N) {
      if (sum) sumArr[sum] = 1;
      return;
    }
    dfs(i + 1, sum + S[i]);
    dfs(i + 1, sum);
  };
  dfs(0, 0);
  for (let i = 1; i <= maxSum + 1; i++) {
    if (!sumArr[i]) return i;
  }
}

console.log(solution(N, S));
