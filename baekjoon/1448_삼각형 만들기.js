const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const straws = input.slice(1).map(Number);

function solution(N, straws) {
  straws.sort((a, b) => b - a);
  let answer = -1;
  for (let i = 0; i < N - 2; i++) {
    const [a, b, c] = [straws[i], straws[i + 1], straws[i + 2]];
    if (a < b + c) {
      answer = a + b + c;
      break;
    }
  }
  console.log(answer);
}

solution(N, straws);
