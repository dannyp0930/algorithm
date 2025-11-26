const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const n = Number(input[0]);
const A = input[1].split(" ").map(Number);
const s = Number(input[2]);

function solution(n, A, s) {
  const visited = Array(n).fill(false);
  visited[s - 1] = true;
  const queue = [s - 1];
  let head = 0;
  let answer = 1;
  while (head < queue.length) {
    const cur = queue[head++];
    const left = cur - A[cur];
    const right = cur + A[cur];
    if (left >= 0 && !visited[left]) {
      visited[left] = true;
      answer++;
      queue.push(left);
    }
    if (right < n && !visited[right]) {
      visited[right] = true;
      answer++;
      queue.push(right);
    }
  }
  console.log(answer);
}

solution(n, A, s);
