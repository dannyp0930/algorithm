const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [R, C, N] = input.shift().split(" ").map(Number);
const grid = input.map((x) => x.split(""));

function solution(R, C, N, grid) {
  const dr = [1, -1, 0, 0];
  const dc = [0, 0, 1, -1];
  let arr = [];
  const checkBomb = () => {
    for (let r = 0; r < R; r++) {
      for (let c = 0; c < C; c++) {
        if (grid[r][c] === "O") arr.push([r, c]);
      }
    }
  };
  const explode = () => {
    for (const [r, c] of arr) {
      grid[r][c] = ".";
      for (let d = 0; d < 4; d++) {
        const [nr, nc] = [r + dr[d], c + dc[d]];
        if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
        grid[nr][nc] = ".";
      }
    }
    arr = [];
  };
  for (let i = 1; i <= N; i++) {
    if (i % 2) {
      if (i !== 1) explode();
      checkBomb();
    } else {
      grid = Array.from(Array(R), () => Array(C).fill("O"));
    }
  }
  console.log(grid.map((x) => x.join("")).join("\n"));
}

solution(R, C, N, grid);
