const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [a, b] = input[0].split(" ").map(Number);
const c = Number(input[1]);
const d = Number(input[2]);

function solution(a, b, c, d) {
  if (a <= c && a * d + b <= c * d) {
    console.log(1);
  } else {
    console.log(0);
  }
}

solution(a, b, c, d);
