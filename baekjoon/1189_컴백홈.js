const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [R, C, K] = input.shift().split(" ").map(Number);
const visit = input.map((a) => a.split("").map((b) => b === "T"));

function solution() {
  const dr = [-1, 0, 1, 0];
  const dc = [0, 1, 0, -1];
  let answer = 0;
  const possible = (r, c) => r >= 0 && r < R && c >= 0 && c < C && !visit[r][c];
  const backtrack = (r, c, cnt) => {
    if (cnt === K) {
      if (r === 0 && c === C - 1) answer++;
      return;
    }
    for (let d = 0; d < 4; d++) {
      const [nr, nc] = [r + dr[d], c + dc[d]];
      if (possible(nr, nc)) {
        visit[nr][nc] = true;
        backtrack(nr, nc, cnt + 1);
        visit[nr][nc] = false;
      }
    }
  };
  visit[R - 1][0] = true;
  backtrack(R - 1, 0, 1);
  console.log(answer);
}

solution();
