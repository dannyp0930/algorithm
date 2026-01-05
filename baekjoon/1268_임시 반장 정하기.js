const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const arr = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(N, arr) {
  const cnt = Array(N).fill(0);
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (i === j) continue;
      for (let k = 0; k < 5; k++) {
        if (arr[i][k] === arr[j][k]) {
          cnt[i]++;
          break;
        }
      }
    }
  }
  let max = 0;
  let answer = 0;
  for (let i = 0; i < N; i++) {
    if (max < cnt[i]) {
      max = cnt[i];
      answer = i;
    }
  }
  console.log(answer + 1);
}

solution(N, arr);
