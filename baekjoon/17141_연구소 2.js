const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const lab = input.map((x) => x.split(" ").map(Number));

function solution(N, M, lab) {
  const virus = [];
  let total = 0;
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      if (lab[r][c] !== 1) {
        total++;
        if (lab[r][c] === 2) {
          virus.push([r, c]);
        }
      }
    }
  }
  const getComb = (n, r) => {
    const res = [];
    const dfs = (arr, idx) => {
      if (arr.length === r) {
        res.push([...arr]);
        return;
      }
      for (let i = idx; i < n; i++) {
        arr.push(i);
        dfs(arr, i + 1);
        arr.pop();
      }
    };
    dfs([], 0);
    return res;
  };
  const bfs = (candi) => {
    const queue = [];
    const visited = Array.from({ length: N }, () => Array(N).fill(-1));
    let cnt = 0;
    for (const idx of candi) {
      const [r, c] = virus[idx];
      queue.push([r, c]);
      visited[r][c] = 0;
      cnt++;
    }
    if (cnt === total) return 0;
    while (queue.length) {
      const [r, c] = queue.shift();
      for (let d = 0; d < 4; d++) {
        const [nr, nc] = [r + dr[d], c + dc[d]];
        if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
        if (lab[nr][nc] === 1) continue;
        if (visited[nr][nc] === -1) {
          visited[nr][nc] = visited[r][c] + 1;
          queue.push([nr, nc]);
          cnt++;
          if (cnt === total) {
            return visited[nr][nc];
          }
        }
      }
    }
    return Infinity;
  };
  const dr = [1, -1, 0, 0];
  const dc = [0, 0, 1, -1];
  let answer = Infinity;
  for (const candi of getComb(virus.length, M)) {
    answer = Math.min(answer, bfs(candi));
  }
  console.log(answer === Infinity ? -1 : answer);
}

solution(N, M, lab);
