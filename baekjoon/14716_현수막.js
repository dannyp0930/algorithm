const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [M, N] = input.shift().split(" ").map(Number);
const banner = input.map((x) => x.split(" ").map(Number));

function solution(M, N, banner) {
  const visited = Array.from({ length: M }, () => Array(N).fill(false));
  const dr = [1, -1, 0, 0, 1, -1, 1, -1];
  const dc = [0, 0, 1, -1, 1, -1, -1, 1];
  const bfs = (queue) => {
    while (queue.length) {
      const [r, c] = queue.shift();
      for (let d = 0; d < 8; d++) {
        const [nr, nc] = [r + dr[d], c + dc[d]];
        if (nr < 0 || nr >= M || nc < 0 || nc >= N) continue;
        if (!banner[nr][nc]) continue;
        if (visited[nr][nc]) continue;
        queue.push([nr, nc]);
        visited[nr][nc] = true;
      }
    }
  };
  let res = 0;
  for (let r = 0; r < M; r++) {
    for (let c = 0; c < N; c++) {
      if (banner[r][c] && !visited[r][c]) {
        res++;
        const queue = [[r, c]];
        visited[r][c] = true;
        bfs(queue);
      }
    }
  }
  console.log(res);
}

solution(M, N, banner);
