const fs = require("fs");
const [N, ...P] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split(" ").map(Number);

function solution(N, P) {
  const prob = P.map((x) => x / 100);
  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  const size = 2 * N + 1;
  const visited = Array.from({ length: size }, () => Array(size).fill(false));
  let answer = 0;
  const dfs = (r, c, cnt, p) => {
    if (cnt === N) {
      answer += p;
      return;
    }
    for (let i = 0; i < 4; i++) {
      if (prob[i] === 0) continue;
      const [nr, nc] = [r + dir[i][0], c + dir[i][1]];
      if (!visited[nr][nc]) {
        visited[nr][nc] = true;
        dfs(nr, nc, cnt + 1, p * prob[i]);
        visited[nr][nc] = false;
      }
    }
  };
  visited[N][N] = true;
  dfs(N, N, 0, 1);
  console.log(answer);
}

solution(N, P);
