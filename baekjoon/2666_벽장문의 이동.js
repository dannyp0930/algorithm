const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const n = Number(input[0]);
const [a, b] = input[1].split(" ").map(Number);
const m = Number(input[2]);
const order = input.slice(3).map(Number);

function solution(n, a, b, m, order) {
  const dp = Array.from({ length: m + 1 }, () =>
    Array.from({ length: n + 1 }, () => Array(n + 1).fill(-1))
  );
  function solve(i, l, r) {
    if (i === m) return 0;
    if (dp[i][l][r] !== -1) return dp[i][l][r];
    const t = order[i];
    if (t === l || t === r) {
      return (dp[i][l][r] = solve(i + 1, l, r));
    }
    const moveLeft = Math.abs(l - t) + solve(i + 1, t, r);
    const moveRight = Math.abs(r - t) + solve(i + 1, l, t);
    return (dp[i][l][r] = Math.min(moveLeft, moveRight));
  }
  console.log(solve(0, a, b));
}

solution(n, a, b, m, order);
