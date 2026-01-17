const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

function solution(input) {
  const [N, M] = input[0].split(" ").map(Number);
  const invalid = Array.from({ length: N + 1 }, () => Array(N + 1).fill(false));
  for (let i = 1; i <= M; i++) {
    const [x, y] = input[i].split(" ").map(Number);
    invalid[x][y] = true;
    invalid[y][x] = true;
  }
  let answer = 0;
  for (let i = 1; i <= N; i++) {
    for (let j = i + 1; j <= N; j++) {
      if (invalid[i][j]) continue;
      for (let k = j + 1; k <= N; k++) {
        if (!invalid[i][k] && !invalid[j][k]) answer++;
      }
    }
  }
  console.log(answer);
}

solution(input);
