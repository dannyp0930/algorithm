const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const IN = input.slice(1, N + 1);
const OUT = input.slice(N + 1);

function solution(N, IN, OUT) {
  let answer = 0;
  const order = new Map();
  for (let i = 0; i < N; i++) {
    order.set(IN[i], i);
  }
  for (let i = 0; i < N; i++) {
    const cur = order.get(OUT[i]);
    for (let j = i + 1; j < N; j++) {
      const next = order.get(OUT[j]);
      if (cur > next) {
        answer++;
        break;
      }
    }
  }
  console.log(answer);
}

solution(N, IN, OUT);
