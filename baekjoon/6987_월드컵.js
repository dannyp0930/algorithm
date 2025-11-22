const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(input) {
  const determin = (arr) => {
    let [winCnt, drawCnt, loseCnt] = [0, 0, 0];
    for (let i = 0; i < 6; i++) {
      const [w, d, l] = arr.slice(i * 3, i * 3 + 3);
      const total = w + d + l;
      if (total !== 5) return false;
      winCnt += w;
      drawCnt += d;
      loseCnt += l;
    }
    if (drawCnt % 2) return false;
    if (winCnt !== loseCnt) return false;
    if ((winCnt + drawCnt + loseCnt) / 2 !== 15) return false;
    const score = Array.from({ length: 6 }, (_, i) => [
      arr[i * 3],
      arr[i * 3 + 1],
      arr[i * 3 + 2],
    ]);
    const matches = [];
    for (let i = 0; i < 6; i++) {
      for (let j = i + 1; j < 6; j++) {
        matches.push([i, j]);
      }
    }
    let possible = false;
    const dfs = (idx) => {
      if (possible) return;
      if (idx === 15) {
        possible = true;
        return;
      }
      const [a, b] = matches[idx];
      for (let i = 0; i < 3; i++) {
        if (score[a][i] && score[b][2 - i]) {
          score[a][i]--;
          score[b][2 - i]--;
          dfs(idx + 1);
          score[a][i]++;
          score[b][2 - i]++;
        }
      }
    };
    dfs(0);
    return possible;
  };
  const result = [];
  for (let i = 0; i < 4; i++) {
    const arr = input[i].split(" ").map(Number);
    if (determin(arr)) result.push(1);
    else result.push(0);
  }
  console.log(result.join(" "));
}

solution(input);
