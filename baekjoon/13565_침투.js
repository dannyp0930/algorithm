const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [M, N] = input.shift().split(" ").map(Number);
const grid = input.map((x) => x.split("").map(Number));

function solution(M, N, grid) {
  const queue = [];
  const visited = Array.from({ length: M }, () => Array(N).fill(false));
  for (let c = 0; c < N; c++) {
    if (!grid[0][c]) {
      queue.push([0, c]);
      visited[0][c] = true;
    }
  }
  const dir = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];
  const isPossible = (r, c) => {
    return 0 <= r && r < M && 0 <= c && c < N && !grid[r][c] && !visited[r][c];
  };
  while (queue.length) {
    const [r, c] = queue.shift();
    if (r === M - 1) {
      return "YES";
    }
    for (let d = 0; d < 4; d++) {
      const [nr, nc] = [r + dir[d][0], c + dir[d][1]];
      if (isPossible(nr, nc)) {
        queue.push([nr, nc]);
        visited[nr][nc] = true;
      }
    }
  }
  return "NO";
}

console.log(solution(M, N, grid));
