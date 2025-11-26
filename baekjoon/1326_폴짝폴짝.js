const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const [a, b] = input[2].split(" ").map(Number);

function solution(N, arr, a, b) {
  const visited = Array(N).fill(-1);
  const queue = [a - 1];
  visited[a - 1] = 0;
  let head = 0;
  while (head < queue.length) {
    const cur = queue[head++];
    if (cur === b - 1) {
      return console.log(visited[cur]);
    }
    const d = arr[cur];
    for (let i = cur + d; i < N; i += d) {
      if (visited[i] === -1) {
        visited[i] = visited[cur] + 1;
        queue.push(i);
      }
    }
    for (let i = cur - d; i >= 0; i -= d) {
      if (visited[i] === -1) {
        visited[i] = visited[cur] + 1;
        queue.push(i);
      }
    }
  }
  return console.log(-1);
}

solution(N, arr, a, b);
