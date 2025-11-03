const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M, T] = input.shift().split(" ").map(Number);
const MAP = input.map((x) => x.split(" ").map(Number));

function solution(N, M, T, MAP) {
  const visited = Array.from({ length: N }, () =>
    Array.from({ length: M }, () => [-1, -1])
  );
  const dr = [1, -1, 0, 0];
  const dc = [0, 0, 1, -1];
  const queue = [[0, 0, 0]];
  visited[0][0][0] = 0;
  while (queue.length) {
    const [r, c, g] = queue.shift();
    for (let d = 0; d < 4; d++) {
      const [nr, nc] = [r + dr[d], c + dc[d]];
      if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
      if (g) {
        if (visited[nr][nc][1] === -1) {
          visited[nr][nc][1] = visited[r][c][1] + 1;
          queue.push([nr, nc, 1]);
        }
      } else {
        if (MAP[nr][nc] !== 1 && visited[nr][nc][0] === -1) {
          const ng = MAP[nr][nc] === 2 ? 1 : 0;
          visited[nr][nc][ng] = visited[r][c][0] + 1;
          queue.push([nr, nc, ng]);
        }
      }
    }
  }
  let answer = T + 1;
  const [noG, withG] = visited[N - 1][M - 1];
  if (noG !== -1) answer = answer > noG ? noG : answer;
  if (withG !== -1) answer = answer > withG ? withG : answer;
  console.log(answer <= T ? answer : "Fail");
}

solution(N, M, T, MAP);
