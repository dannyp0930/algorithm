const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [R, C] = input.shift().split(" ").map(Number);
const MAP = input.map((x) => x.split(""));

function solution(R, C, MAP) {
  const visited = Array.from({ length: R }, () => Array(C).fill(false));
  const answer = [0, 0];
  const dr = [1, -1, 0, 0];
  const dc = [0, 0, 1, -1];
  const bfs = (x, y) => {
    let s = 0,
      w = 0;
    const queue = [[x, y]];
    visited[x][y] = true;
    if (MAP[x][y] === "v") w++;
    else if (MAP[x][y] === "k") s++;
    while (queue.length) {
      const [r, c] = queue.shift();
      for (let d = 0; d < 4; d++) {
        const [nr, nc] = [r + dr[d], c + dc[d]];
        if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
        if (MAP[nr][nc] === "#") continue;
        if (visited[nr][nc]) continue;
        if (MAP[nr][nc] === "v") w++;
        else if (MAP[nr][nc] === "k") s++;
        visited[nr][nc] = true;
        queue.push([nr, nc]);
      }
    }
    if (s || w) {
      if (s > w) answer[0] += s;
      else answer[1] += w;
    }
  };
  for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
      if (!visited[r][c] && MAP[r][c] !== "#") {
        bfs(r, c);
      }
    }
  }
  console.log(answer.join(" "));
}

solution(R, C, MAP);
