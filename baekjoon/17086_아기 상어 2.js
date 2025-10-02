const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [N, M] = input.shift().split(" ").map(Number);
  const graph = [];
  const queue = [];
  const visit = Array.from(Array(N), () => Array(M).fill(-1));
  for (let i = 0; i < N; i++) {
    const arr = input[i].split(" ").map(Number);
    graph.push(arr);
    for (let j = 0; j < M; j++) {
      if (arr[j]) {
        queue.push([i, j]);
        visit[i][j] = 0;
      }
    }
  }
  const dr = [1, -1, 0, 0, 1, -1, 1, -1];
  const dc = [0, 0, 1, -1, 1, -1, -1, 1];
  const possible = (r, c) => {
    return 0 <= r && r < N && 0 <= c && c < M && visit[r][c] === -1;
  };
  let answer = 0;
  while (queue.length) {
    const [r, c] = queue.shift();
    for (let d = 0; d < 8; d++) {
      const [nr, nc] = [r + dr[d], c + dc[d]];
      if (possible(nr, nc)) {
        queue.push([nr, nc]);
        visit[nr][nc] = visit[r][c] + 1;
        answer = answer < visit[nr][nc] ? visit[nr][nc] : answer;
      }
    }
  }
  console.log(answer);
}

solution();
