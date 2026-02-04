const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const S = input[0];
const N = Number(input[1]);
const rings = input.slice(2);

function solution(S, N, rings) {
  let answer = 0;
  for (let i = 0; i < N; i++) {
    const ring = rings[i];
    const circle = ring + ring;
    if (circle.includes(S)) {
      answer++;
    }
  }
  console.log(answer);
}

solution(S, N, rings);
