const fs = require("fs");
const [A, B, N, M] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split(" ").map(Number);

function solution(A, B, N, M) {
  const visited = Array(100001).fill(-1);
  const queue = [N];
  visited[N] = 0;
  let head = 0;
  const dir = [1, -1, A, -A, B, -B, A, B];
  while (head < queue.length) {
    const x = queue[head++];
    if (x === M) {
      console.log(visited[M]);
      return;
    }
    for (let d = 0; d < 8; d++) {
      let nx = x;
      if (d > 5) nx *= dir[d];
      else nx += dir[d];
      if (0 <= nx && nx <= 100000 && visited[nx] === -1) {
        visited[nx] = visited[x] + 1;
        queue.push(nx);
      }
    }
  }
}

solution(A, B, N, M);
