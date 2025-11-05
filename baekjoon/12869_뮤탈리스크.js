const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const SCV = input[1].split(" ").map(Number);

function getPermutation(n) {
  const res = [];
  const visited = Array(n).fill(false);
  const dfs = (arr) => {
    if (arr.length === n) {
      res.push([...arr]);
      return;
    }
    for (let i = 0; i < n; i++) {
      if (visited[i]) continue;
      visited[i] = true;
      dfs([...arr, i]);
      visited[i] = false;
    }
  };
  dfs([]);
  return res;
}

function solution(N, SCV) {
  const atk = [9, 3, 1];
  const visited = Array.from({ length: 61 }, () =>
    Array.from({ length: 61 }, () => Array(61).fill(false))
  );
  while (SCV.length < 3) SCV.push(0);
  const queue = [[...SCV, 0]];
  visited[SCV[0]][SCV[1]][SCV[2]] = true;
  while (queue.length) {
    const [a, b, c, cnt] = queue.shift();
    if (a <= 0 && b <= 0 && c <= 0) {
      console.log(cnt);
      return;
    }
    for (const [x, y, z] of getPermutation(3)) {
      const na = Math.max(0, a - atk[x]);
      const nb = Math.max(0, b - atk[y]);
      const nc = Math.max(0, c - atk[z]);
      if (!visited[na][nb][nc]) {
        visited[na][nb][nc] = true;
        queue.push([na, nb, nc, cnt + 1]);
      }
    }
  }
}

solution(N, SCV);
