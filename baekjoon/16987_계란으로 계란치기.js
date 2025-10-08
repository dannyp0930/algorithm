const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const N = Number(input.shift());
  const eggs = input.map((a) => a.split(" ").map(Number));
  const durabilities = eggs.map((a) => a[0]);
  let answer = 0;
  const crash = (i, j, arr) => {
    arr[i] -= eggs[j][1];
    arr[j] -= eggs[i][1];
    return arr;
  };
  const backtrack = (idx, arr) => {
    if (idx === N) {
      const cnt = arr.reduce((a, c) => (a + (c <= 0 ? 1 : 0)), 0);
      answer = cnt > answer ? cnt : answer;
      return;
    }
    if (arr[idx] <= 0) {
      backtrack(idx + 1, [...arr]);
      return;
    }
    let flag = false;
    for (let i = 0; i < N; i++) {
      if (i !== idx && arr[i] > 0) {
        flag = true;
        backtrack(idx + 1, crash(i, idx, [...arr]));
      }
    }
    if (!flag) {
      answer = N - 1 > answer ? N - 1 : answer;
      return;
    }
  };
  backtrack(0, durabilities);
  console.log(answer);
}

solution();
