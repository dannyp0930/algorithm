const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [N, M] = input.shift().split(" ").map(Number);
  const A = input.map(Number).sort((a, b) => a - b);
  let s = 0,
    e = 0;
  let answer = 2000000000;
  while (e < N) {
    const diff = A[e] - A[s];
    if (diff >= M) {
      answer = answer > diff ? diff : answer;
      s++;
    } else {
      e++;
    }
  }
  console.log(answer);
}

solution();
