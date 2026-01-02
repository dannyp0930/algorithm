const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const arr = input.slice(1);

function solution(N, M, arr) {
  const visited = Array.from({ length: N }, () => Array(M).fill(false));
  let answer = 0;
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < M; c++) {
      if (!visited[r][c]) {
        answer++;
        visited[r][c] = true;
        const queue = [[r, c]];
        let head = 0;
        while (head < queue.length) {
          const [x, y] = queue[head++];
          if (arr[x][y] === "-") {
            if (y + 1 < M && arr[x][y + 1] === "-") {
              visited[x][y + 1] = true;
              queue.push([x, y + 1]);
            }
          } else {
            if (x + 1 < N && arr[x + 1][y] === "|") {
              visited[x + 1][y] = true;
              queue.push([x + 1, y]);
            }
          }
        }
      }
    }
  }
  console.log(answer);
}

solution(N, M, arr);
