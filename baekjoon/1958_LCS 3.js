const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [a, b, c] = input;

function solution(a, b, c) {
  const n = a.length;
  const m = b.length;
  const l = c.length;
  const dp = Array.from({ length: n + 1 }, () =>
    Array.from({ length: m + 1 }, () => Array(l + 1).fill(0))
  );
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      for (let k = 1; k <= l; k++) {
        if (a[i - 1] === b[j - 1] && b[j - 1] === c[k - 1]) {
          dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1;
        } else {
          dp[i][j][k] = Math.max(
            dp[i - 1][j][k],
            dp[i][j - 1][k],
            dp[i][j][k - 1]
          );
        }
      }
    }
  }
  console.log(dp[n][m][l]);
}

solution(a, b, c);
