const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const pos = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

function solution(N, pos) {
  console.log(pos[(N - 1) >> 1])
  
}

solution(N, pos);
