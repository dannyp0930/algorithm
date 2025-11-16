const fs = require("fs");
const [n, k] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split(" ").map(Number);

function solution(n, k) {
  let answer = "-1";
  let cnt = 0;
  const dfs = (tot, str) => {
    if (tot === n) {
      cnt++;
      if (cnt === k) {
        answer = str;
        return true;
      }
      return false;
    }
    for (let i = 1; i <= 3; i++) {
      if (tot + i <= n) {
        if (dfs(tot + i, str ? `${str}+${i}` : `${i}`)) return true;
      }
    }
    return false;
  };
  dfs(0, "");
  console.log(answer);
}

solution(n, k);
