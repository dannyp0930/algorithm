const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input.shift());
const MAP = input.map((x) => x.split(" "));

function solution(N, MAP) {
  const teachers = [];
  const blanks = [];
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      if (MAP[r][c] === "T") teachers.push([r, c]);
      if (MAP[r][c] === "X") blanks.push([r, c]);
    }
  }
  const dr = [1, -1, 0, 0];
  const dc = [0, 0, 1, -1];
  const watch = (r, c) => {
    for (let d = 0; d < 4; d++) {
      let [nr, nc] = [r, c];
      while (true) {
        nr += dr[d];
        nc += dc[d];
        if (nr < 0 || nr >= N || nc < 0 || nc >= N || MAP[nr][nc] === "O")
          break;
        if (MAP[nr][nc] === "S") return true;
      }
    }
    return false;
  };
  const check = () => {
    for (const [r, c] of teachers) {
      if (watch(r, c)) return false;
    }
    return true;
  };
  const dfs = (idx, cnt) => {
    if (cnt === 3) return check();
    for (let i = idx; i < blanks.length; i++) {
      const [r, c] = blanks[i];
      MAP[r][c] = "O";
      if (dfs(i + 1, cnt + 1)) return true;
      MAP[r][c] = "X";
    }
    return false;
  };
  console.log(dfs(0, 0) ? "YES" : "NO");
}

solution(N, MAP);
