const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

function solution(input) {
  const N = Number(input[0]);
  const MAP = input.slice(1).map((x) => x.split(" ").map(Number));
  const visited = Array.from({ length: N }, () => Array(N).fill(false));
  const queue = [[0, 0]];
  visited[0][0] = true;
  let head = 0;
  const dr = [1, 0];
  const dc = [0, 1];
  while (head < queue.length) {
    const [r, c] = queue[head++];
    const w = MAP[r][c];
    if (w === -1) {
      console.log("HaruHaru");
      return;
    }
    for (let d = 0; d < 2; d++) {
      const [nr, nc] = [r + dr[d] * w, c + dc[d] * w];
      if (nr >= N || nc >= N) continue;
      if (visited[nr][nc]) continue;
      queue.push([nr, nc]);
      visited[nr][nc] = true;
    }
  }
  console.log("Hing");
}

solution(input);
