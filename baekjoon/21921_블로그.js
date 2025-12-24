const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, X] = input[0].split(" ").map(Number);
const V = input[1].split(" ").map(Number);

function solution(N, X, V) {
  let sum = V.slice(0, X).reduce((a, c) => a + c);
  let max = sum;
  let cnt = 1;
  for (let i = 0; i + X < N; i++) {
    sum += V[i + X] - V[i];
    if (sum === max) {
      cnt++;
    } else if (sum > max) {
      max = sum;
      cnt = 1;
    }
  }
  if (max) {
    console.log(max);
    console.log(cnt);
  } else {
    console.log("SAD");
  }
}

solution(N, X, V);
