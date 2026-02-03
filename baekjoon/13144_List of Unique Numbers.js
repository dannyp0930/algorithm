const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);

function solution(N, arr) {
  const visited = Array(100001).fill(false);
  let answer = 0;
  let l = 0;
  for (let r = 0; r < N; r++) {
    while (visited[arr[r]]) {
      visited[arr[l]] = false;
      l++;
    }
    visited[arr[r]] = true;
    answer += r - l + 1;
  }
  console.log(answer);
}

solution(N, arr);
