const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, K, B] = input.shift().split(" ").map(Number);
const breakdowns = input.map(Number);

function solution(N, K, B, breakdowns) {
  const lights = Array(N).fill(0);
  for (const num of breakdowns) {
    lights[num - 1] = 1;
  }
  let total = lights.slice(0, K).reduce((a, c) => a + c);
  let answer = total;
  for (let i = 0; i < N - K; i++) {
    total += lights[i + K] - lights[i];
    answer = answer > total ? total : answer;
  }
  console.log(answer);
}

solution(N, K, B, breakdowns);
