const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input.shift());
const dice = input.map((x) => x.split(" ").map(Number));

function solution(N, dice) {
  const opposite = [5, 3, 4, 1, 2, 0];
  let answer = 0;
  for (let s = 0; s < 6; s++) {
    let top = dice[0][opposite[s]];
    let sum = Math.max(
      ...dice[0].filter((_, i) => i !== s && i !== opposite[s])
    );
    for (let i = 1; i < N; i++) {
      const d = dice[i];
      const bIdx = d.indexOf(top);
      const tIdx = opposite[bIdx];
      top = d[tIdx];
      sum += Math.max(...d.filter((_, i) => i !== tIdx && i !== bIdx));
    }
    answer = answer > sum ? answer : sum;
  }
  console.log(answer);
}

solution(N, dice);
