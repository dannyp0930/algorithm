const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function binarySearch(input) {
  let idx = 0;
  let T = Number(input[idx++]);
  const res = [];
  while (T--) {
    const [N, M] = input[idx++].split(" ").map(Number);
    const A = input[idx++].split(" ").map(Number);
    const B = input[idx++]
      .split(" ")
      .map(Number)
      .sort((a, b) => a - b);
    let answer = 0;
    for (let i = 0; i < N; i++) {
      let [l, r] = [0, M - 1];
      const target = A[i];
      let cnt = 0;
      while (l <= r) {
        const m = (l + r) >> 1;
        if (B[m] < target) {
          l = m + 1;
          cnt = m + 1;
        } else {
          r = m - 1;
        }
      }
      answer += cnt;
    }
    res.push(answer);
  }
  console.log(res.join("\n"));
}

function twoPointer(input) {
  let idx = 0;
  let T = Number(input[idx++]);
  const res = [];
  while (T--) {
    const [N, M] = input[idx++].split(" ").map(Number);
    const A = input[idx++]
      .split(" ")
      .map(Number)
      .sort((a, b) => a - b);
    const B = input[idx++]
      .split(" ")
      .map(Number)
      .sort((a, b) => a - b);
    let answer = 0;
    let b = 0;
    for (let a = 0; a < N; a++) {
      while (b < M && B[b] < A[a]) {
        b++;
      }
      answer += b;
    }
    res.push(answer);
  }
  console.log(res.join("\n"));
}

binarySearch(input);
twoPointer(input);
