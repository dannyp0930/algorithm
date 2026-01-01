const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const A = input.slice(1).map(Number);

function solution(N, A) {
  A.sort((a, b) => a - b);
  console.log(A.join("\n"));
}

solution(N, A);
