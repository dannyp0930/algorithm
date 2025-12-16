const fs = require("fs");
const N = Number(
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim()
);

function solution(N) {
  console.log((N ** 0.5) >> 0);
}

solution(N);
