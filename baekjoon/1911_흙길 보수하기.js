const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, L] = input.shift().split(" ").map(Number);
const pools = input.map((x) => x.split(" ").map(Number));

function solution(N, L, pools) {
  pools.sort((a, b) => a[0] - b[0]);
  let answer = 0;
  let idx = 0;
  for (const [a, b] of pools) {
    if (idx < a) idx = a;
    if (idx >= b) continue;
    const cnt = Math.ceil((b - idx) / L);
    answer += cnt;
    idx += cnt * L;
  }
  console.log(answer);
}

solution(N, L, pools);
