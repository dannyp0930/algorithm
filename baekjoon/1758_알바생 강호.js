const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const tips = input.slice(1).map(Number);

function solution(N, tips) {
  let answer = 0;
  tips.sort((a, b) => b - a);
  for (let i = 0; i < N; i++) {
    const tip = tips[i] - i;
    answer += tip > 0 ? tip : 0;
  }
  console.log(answer);
}

solution(N, tips);
