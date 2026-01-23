const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const [N, K] = input[0].split(" ").map(Number);
const A = input[1].split(" ").map(Number);

function solution(N, K, A) {
  let answer = 0;
  const visited = Array(N).fill(false);
  const backtrack = (day, cur) => {
    if (day === N) {
      answer++;
      return;
    }
    for (let i = 0; i < N; i++) {
      if (!visited[i]) {
        const now = cur - K + A[i];
        if (now >= 500) {
          visited[i] = true;
          backtrack(day + 1, now);
          visited[i] = false;
        }
      }
    }
  };
  backtrack(0, 500);
  console.log(answer);
}

solution(N, K, A);
