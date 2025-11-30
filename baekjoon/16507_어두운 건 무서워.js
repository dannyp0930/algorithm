const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [R, C, Q] = input[0].split(" ").map(Number);
const photo = input.slice(1, R + 1).map((x) => x.split(" ").map(Number));
const query = input.slice(R + 1).map((x) => x.split(" ").map(Number));

function solution(R, C, Q, photo, query) {
  const prefix = Array.from({ length: R + 1 }, () => Array(C + 1).fill(0));
  for (let r = 1; r <= R; r++) {
    for (let c = 1; c <= C; c++) {
      prefix[r][c] =
        photo[r - 1][c - 1] +
        prefix[r - 1][c] +
        prefix[r][c - 1] -
        prefix[r - 1][c - 1];
    }
  }
  const res = [];
  for (const [r1, c1, r2, c2] of query) {
    const sum =
      prefix[r2][c2] -
      prefix[r1 - 1][c2] -
      prefix[r2][c1 - 1] +
      prefix[r1 - 1][c1 - 1];
    const cnt = (r2 - r1 + 1) * (c2 - c1 + 1);
    res.push((sum / cnt) >> 0);
  }
  console.log(res.join("\n"));
}

solution(R, C, Q, photo, query);
