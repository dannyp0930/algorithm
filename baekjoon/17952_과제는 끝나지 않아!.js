const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const assignments = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(N, assignments) {
  const stack = [];
  let answer = 0;
  for (let i = 0; i < N; i++) {
    const assignment = assignments[i];
    if (assignment[0] === 1) {
      const [_, score, time] = assignment;
      stack.push([score, time]);
    }
    if (stack.length) {
      stack[stack.length - 1][1]--;
      if (stack[stack.length - 1][1] === 0) {
        const [score, _] = stack.pop();
        answer += score;
      }
    }
  }
  console.log(answer);
}

solution(N, assignments);
