const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const query = input.slice(1);

function solution(N, query) {
  let logs = new Set();
  let answer = 0;
  for (let i = 1; i < N; i++) {
    const q = query[i];
    if (q === "ENTER") {
      logs = new Set();
      continue;
    }
    if (!logs.has(q)) {
      logs.add(q);
      answer++;
    }
  }
  console.log(answer);
}

solution(N, query);
