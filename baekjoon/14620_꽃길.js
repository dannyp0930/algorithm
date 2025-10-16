const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = +input.shift();
const ground = input.map((x) => x.split(" ").map(Number));

function solution(N, ground) {
  let answer = Infinity;
  const visit = Array.from({ length: N }, () => Array(N).fill(false));
  const dr = [1, -1, 0, 0, 0];
  const dc = [0, 0, 1, -1, 0];
  const possible = (r, c) => {
    for (let d = 0; d < 5; d++) {
      const [nr, nc] = [r + dr[d], c + dc[d]];
      if (visit[nr][nc]) return false;
    }
    return true;
  };
  const dfs = (cnt, cost) => {
    if (cnt === 3) {
      answer = answer > cost ? cost : answer;
      return;
    }
    for (let r = 1; r < N - 1; r++) {
      for (let c = 1; c < N - 1; c++) {
        if (possible(r, c)) {
          let plus = 0;
          for (let d = 0; d < 5; d++) {
            const [nr, nc] = [r + dr[d], c + dc[d]];
            visit[nr][nc] = true;
            plus += ground[nr][nc];
          }
          dfs(cnt + 1, cost + plus);
          for (let d = 0; d < 5; d++) {
            const [nr, nc] = [r + dr[d], c + dc[d]];
            visit[nr][nc] = false;
          }
        }
      }
    }
  };
  dfs(0, 0);
  console.log(answer);
}

solution(N, ground);
