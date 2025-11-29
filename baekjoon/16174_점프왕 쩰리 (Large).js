const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const MAP = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(N, MAP) {
  const visited = Array.from({ length: N }, () => Array(N).fill(false));
  const queue = [[0, 0]];
  visited[0][0] = true;
  let head = 0;
  const dr = [0, 1];
  const dc = [1, 0];
  while (head < queue.length) {
    const [r, c] = queue[head++];
    if (r === N - 1 && c === N - 1) {
      return console.log("HaruHaru");
    }
    const d = MAP[r][c];
    if (d === 0) continue;
    for (let i = 0; i < 2; i++) {
      const [nr, nc] = [r + dr[i] * d, c + dc[i] * d];
      if (nr < N && nc < N && !visited[nr][nc]) {
        visited[nr][nc] = true;
        queue.push([nr, nc]);
      }
    }
  }
  return console.log("Hing");
}

solution(N, MAP);
