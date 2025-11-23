const fs = require("fs");
const N =
  process.platform === "linux"
    ? Number(fs.readFileSync(0, "utf-8").toString().trim())
    : Number(fs.readFileSync("input.txt").toString().trim());

function solution(N) {
  const result = [];
  const dfs = (last, val) => {
    result.push(val);
    for (let i = 0; i < last; i++) {
      dfs(i, val * 10 + i);
    }
  };
  for (let i = 0; i < 10; i++) {
    dfs(i, i);
  }
  result.sort((a, b) => a - b);
  console.log(result.length < N ? -1 : result[N - 1]);
}

solution(N);
