const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = input[0];
const S = input[1];

function solution(N, S) {
  const size = 2 * N + 1;
  const origin = size >> 1;
  const MAP = Array.from({ length: size }, () => Array(size).fill("#"));
  const dr = [1, 0, -1, 0];
  const dc = [0, -1, 0, 1];
  let r = origin,
    c = origin,
    dir = 0;
  let minR = r,
    maxR = r,
    minC = c,
    maxC = c;
  MAP[r][c] = ".";
  for (const ch of S) {
    if (ch === "L") {
      dir = (dir + 3) % 4;
    } else if (ch === "R") {
      dir = (dir + 1) % 4;
    } else {
      r += dr[dir];
      c += dc[dir];
      MAP[r][c] = ".";
      minR = minR > r ? r : minR;
      maxR = maxR < r ? r : maxR;
      minC = minC > c ? c : minC;
      maxC = maxC < c ? c : maxC;
    }
  }
  for (let r = minR; r <= maxR; r++) {
    console.log(MAP[r].slice(minC, maxC + 1).join(""));
  }
}

solution(N, S);
