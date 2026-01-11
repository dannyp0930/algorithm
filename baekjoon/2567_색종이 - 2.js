const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .trim()
  .split("\n");

const n = Number(input[0]);
const pos = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(n, pos) {
  const grid = Array.from({ length: 102 }, () => Array(102).fill(false));
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];
  for (let i = 0; i < n; i++) {
    const [x, y] = pos[i];
    for (let i = x; i < x + 10; i++) {
      for (let j = y; j < y + 10; j++) {
        grid[i][j] = true;
      }
    }
  }
  let answer = 0;
  for (let i = 1; i < 101; i++) {
    for (let j = 1; j < 101; j++) {
      if (grid[i][j]) {
        for (let d = 0; d < 4; d++) {
          if (!grid[i + dx[d]][j + dy[d]]) answer++;
        }
      }
    }
  }
  console.log(answer);
}

solution(n, pos);
