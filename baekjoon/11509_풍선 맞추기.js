const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const H = input[1].split(" ").map(Number);

function solution(N, H) {
  const arr = Array(1000001).fill(0);
  let answer = 0;
  for (const h of H) {
    if (arr[h]) arr[h]--;
    else answer++;
    arr[h - 1]++;
  }
  console.log(answer);
}

solution(N, H);
