const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const MAP = input.slice(1, N + 1).map((x) => x.split(" ").map(Number));
const K = Number(input[N + 1]);
const SEC = input.slice(N + 2).map((x) => x.split(" ").map(Number));

function solution(N, M, MAP, K, SEC) {
  const prefix = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));
  for (let r = 1; r <= N; r++) {
    for (let c = 1; c <= M; c++) {
      prefix[r][c] =
        MAP[r - 1][c - 1] +
        prefix[r][c - 1] +
        prefix[r - 1][c] -
        prefix[r - 1][c - 1];
    }
  }
  const res = [];
  for (const [x1, y1, x2, y2] of SEC) {
    res.push(
      prefix[x2][y2] -
        prefix[x1 - 1][y2] -
        prefix[x2][y1 - 1] +
        prefix[x1 - 1][y1 - 1]
    );
  }
  console.log(res.join("\n"));
}

solution(N, M, MAP, K, SEC);
