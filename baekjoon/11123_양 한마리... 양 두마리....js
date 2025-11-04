const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(input) {
  const T = Number(input.shift());
  let s = 0;
  const answer = [];
  const dh = [1, -1, 0, 0];
  const dw = [0, 0, 1, -1];
  for (let t = 0; t < T; t++) {
    const [H, W] = input[s].split(" ").map(Number);
    const grid = input.slice(s + 1, s + H + 1).map((x) => x.split(""));
    const visited = Array.from({ length: H }, () => Array(W).fill(false));
    let res = 0;
    for (let i = 0; i < H; i++) {
      for (let j = 0; j < W; j++) {
        if (!visited[i][j] && grid[i][j] === "#") {
          res++;
          const queue = [[i, j]];
          visited[i][j] = true;
          while (queue.length) {
            const [h, w] = queue.shift();
            for (let d = 0; d < 4; d++) {
              const [nh, nw] = [h + dh[d], w + dw[d]];
              if (nh < 0 || nh >= H || nw < 0 || nw >= W) continue;
              if (visited[nh][nw] || grid[nh][nw] === ".") continue;
              visited[nh][nw] = true;
              queue.push([nh, nw]);
            }
          }
        }
      }
    }
    answer.push(res);
    s += H + 1;
  }
  console.log(answer.join("\n"));
}

solution(input);
