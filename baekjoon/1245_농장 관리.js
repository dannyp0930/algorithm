const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const MAP = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(N, M, MAP) {
  const visited = Array.from({ length: N }, () => Array(M).fill(false));
  let answer = 0;
  const dr = [1, -1, 0, 0, 1, -1, 1, -1];
  const dc = [0, 0, 1, -1, 1, -1, -1, 1];
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < M; c++) {
      if (!visited[r][c] && MAP[r][c]) {
        const queue = [[r, c]];
        let head = 0;
        let flag = true;
        visited[r][c] = true;
        while (head < queue.length) {
          const [x, y] = queue[head++];
          for (let d = 0; d < 8; d++) {
            const [nx, ny] = [x + dr[d], y + dc[d]];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if (MAP[x][y] < MAP[nx][ny]) flag = false;
            if (!visited[nx][ny] && MAP[x][y] === MAP[nx][ny]) {
              visited[nx][ny] = true;
              queue.push([nx, ny]);
            }
          }
        }
        if (flag) answer++;
      }
    }
  }
  console.log(answer);
}

solution(N, M, MAP);
