const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const t = Number(input.shift());

function solution(t, input) {
  let idx = 0;
  while (t) {
    const [l, n] = input[idx].split(" ").map(Number);
    const ants = input.slice(idx + 1, idx + n + 1).map(Number);
    let min = 0;
    let max = 0;
    for (const x of ants) {
      min = Math.max(min, Math.min(x, l - x));
      max = Math.max(max, x, l - x);
    }
    console.log(min, max);
    t--;
    idx += n + 1;
  }
}

solution(t, input);
