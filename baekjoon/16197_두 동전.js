const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input.shift(0).split(" ").map(Number);
const board = input.map((x) => x.split(""));

function solution(N, M, board) {
  const coins = [];
  const visited = Array.from({ length: N }, () =>
    Array.from({ length: M }, () =>
      Array.from({ length: N }, () => Array(M).fill(false))
    )
  );
  const getCoins = () => {
    let cnt = 0;
    for (let r = 0; r < N; r++) {
      for (let c = 0; c < M; c++) {
        if (board[r][c] === "o") {
          coins.push(r, c);
          cnt++;
          if (cnt === 2) {
            const [r1, c1, r2, c2] = coins;
            visited[r1][c1][r2][c2] = true;
            visited[r2][c2][r1][c1] = true;
            return;
          }
        }
      }
    }
    return;
  };
  getCoins();
  const outBound = (r, c) => r < 0 || r >= N || c < 0 || c >= M;
  const queue = [[...coins, 0]];
  let head = 0;
  const dr = [0, 0, -1, 1];
  const dc = [-1, 1, 0, 0];
  while (head < queue.length) {
    const [r1, c1, r2, c2, cnt] = queue[head++];
    for (let d = 0; d < 4; d++) {
      let [nr1, nc1] = [r1 + dr[d], c1 + dc[d]];
      let [nr2, nc2] = [r2 + dr[d], c2 + dc[d]];
      const o1 = outBound(nr1, nc1);
      const o2 = outBound(nr2, nc2);
      if (!o1 && !o2) {
        if (board[nr1][nc1] === "#") [nr1, nc1] = [r1, c1];
        if (board[nr2][nc2] === "#") [nr2, nc2] = [r2, c2];
        if (!visited[nr1][nc1][nr2][nc2] && cnt < 10) {
          visited[nr1][nc1][nr2][nc2] = true;
          visited[nr2][nc2][nr1][nc1] = true;
          queue.push([nr1, nc1, nr2, nc2, cnt + 1]);
        }
      } else if (o1 ^ o2) {
        if (cnt + 1 > 10) {
          console.log(-1);
          return;
        }
        console.log(cnt + 1);
        return;
      }
    }
  }
  console.log(-1);
  return;
}

solution(N, M, board);
