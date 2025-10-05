const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const N = Number(input[0]);
  const S = input[1].split(" ").map(Number);
  let s = 0,
    e = 0,
    cnt = 0,
    type = 0;
  const fruit = Array(10).fill(0);
  let answer = 0;
  while (e < N) {
    if (!fruit[S[e]]) type++;
    fruit[S[e]]++;
    cnt++;
    if (type > 2) {
      while (type > 2) {
        fruit[S[s]]--;
        if (!fruit[S[s]]) type--;
        cnt--;
        s++;
      }
    }
    answer = cnt > answer ? cnt : answer;
    e++;
  }
  console.log(answer);
}

solution();
