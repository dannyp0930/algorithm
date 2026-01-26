const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const cows = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(cows) {
  let answer = 0;
  cows.sort((a, b) => a[0] - b[0]);
  for (const [arrival, process] of cows) {
    if (answer < arrival) answer = arrival;
    answer += process;
  }
  console.log(answer);
}

solution(cows);
