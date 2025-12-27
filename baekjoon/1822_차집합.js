const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [nA, nB] = input[0].split(" ").map(Number);
const A = new Set(input[1].split(" ").map(Number));
const B = new Set(input[2].split(" ").map(Number));

function solution(nA, nB, A, B) {
  const res = [];
  for (let a of A) {
    if (!B.has(a)) {
      res.push(a);
    }
  }
  if (res.length) {
    res.sort((a, b) => a - b);
    console.log(res.length);
    console.log(res.join(" "));
  } else {
    console.log(0);
  }
}

solution(nA, nB, A, B);
