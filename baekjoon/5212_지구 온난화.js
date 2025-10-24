const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [R, C] = input.shift().split(" ").map(Number);
const MAP = input.map((x) => x.split(""));

function solution(R, C, MAP) {
  const dir = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];
  const isSurround = (r, c) => {
    let cnt = 0;
    for (let d = 0; d < 4; d++) {
      const [nr, nc] = [r + dir[d][0], c + dir[d][1]];
      if (!(0 <= nr && nr < R && 0 <= nc && nc < C) || MAP[nr][nc] === ".") {
        cnt++;
      }
    }
    return cnt >= 3;
  };
  const arr = [];
  for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
      if (MAP[r][c] === "X" && isSurround(r, c)) {
        arr.push([r, c]);
      }
    }
  }
  for (const [r, c] of arr) {
    MAP[r][c] = ".";
  }
  let [sr, sc, er, ec] = [R, C, -1, -1];
  for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
      if (MAP[r][c] === "X") {
        sr = Math.min(sr, r);
        sc = Math.min(sc, c);
        er = Math.max(er, r);
        ec = Math.max(ec, c);
      }
    }
  }
  for (let r = sr; r <= er; r++) {
    console.log(MAP[r].slice(sc, ec + 1).join(""));
  }
}

solution(R, C, MAP);
