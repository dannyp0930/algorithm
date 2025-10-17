const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [_N, M] = input[0].split(" ").map(Number);
const books = input[1].split(" ").map(Number);

function solution(M, books) {
  const minus = books.filter(a => a < 0).map(a => -a).sort((a, b) => b - a);
  const plus = books.filter(a => a > 0).sort((a, b) => b - a);
  let answer = -Math.max(plus[0] ?? 0, minus[0] ?? 0);
  for (let i = 0; i < minus.length; i += M) answer += 2 * minus[i];
  for (let i = 0; i < plus.length; i += M) answer += 2 * plus[i];
  console.log(answer);
}

solution(M, books);
