const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, L, R, X] = input[0].split(" ").map(Number);
const A = input[1].split(" ").map(Number);

function solution(N, L, R, X, A) {
  let answer = 0;
  for (let i = 1; i < 1 << N; i++) {
    let cnt = 0;
    let maxL = 0;
    let minL = 1000000;
    let totL = 0;
    for (let j = 0; j < N; j++) {
      if ((i & (1 << j)) !== 0) {
        const level = A[j];
        cnt++;
        if (maxL < level) maxL = level;
        if (minL > level) minL = level;
        totL += level;
      }
    }
    if (cnt >= 2 && L <= totL && totL <= R && maxL - minL >= X) {
      answer++;
    }
  }
  console.log(answer);
}

solution(N, L, R, X, A);
