const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const C = Number(input[0]);
const arr = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(C, arr) {
  let t = 0;
  while (C--) {
    const S = arr.slice(t, t + 11);
    const visited = Array(11).fill(false);
    let res = 0;
    const backtrack = (pos, abil) => {
      if (pos === 11) {
        if (abil > res) res = abil;
        return;
      }
      for (let i = 0; i < 11; i++) {
        if (!visited[i] && S[i][pos]) {
          visited[i] = true;
          backtrack(pos + 1, abil + S[i][pos]);
          visited[i] = false;
        }
      }
    };
    backtrack(0, 0);
    console.log(res);
    t += 11;
  }
}

solution(C, arr);
