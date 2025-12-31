const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const rank = input.slice(1).map(Number);

function solution(N, rank) {
  rank.sort((a, b) => a - b);
  let res = 0;
  for (let i = 0; i < N; i++) {
    res += Math.abs(i + 1 - rank[i]);
  }
  console.log(res);
}

solution(N, rank);
