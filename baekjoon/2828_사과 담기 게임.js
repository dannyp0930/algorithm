const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const J = Number(input[1]);
const pos = input.slice(2).map(Number);

function solution(N, M, J, pos) {
  let [l, r] = [1, M];
  let ans = 0;
  for (let i = 0; i < J; i++) {
    const p = pos[i];
    if (p > r) {
      ans += p - r;
      l += p - r;
      r = p;
    } else if (p < l) {
      ans += l - p;
      r -= l - p;
      l = p;
    }
  }
  console.log(ans);
}

solution(N, M, J, pos);
