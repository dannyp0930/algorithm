const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const k = Number(input[0]);
const g = input[1].split(" ").map(Number);

function solution(k, g) {
  const S = g.reduce((a, c) => a + c);
  const w = new Set();
  const dfs = (idx, tot) => {
    if (idx === k) {
      if (tot) w.add(tot);
      return;
    }
    dfs(idx + 1, tot + g[idx]);
    dfs(idx + 1, Math.abs(tot - g[idx]));
    dfs(idx + 1, tot);
  };
  dfs(0, 0);
  console.log(S - w.size);
}

solution(k, g);
