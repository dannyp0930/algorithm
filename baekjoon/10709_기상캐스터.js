const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [H, W] = input[0].split(" ").map(Number);
const arr = input.slice(1);

function solution(H, W, arr) {
  const res = Array.from({ length: H }, () => Array(W).fill(-1));
  for (let r = 0; r < H; r++) {
    let idx = -1;
    for (let c = 0; c < W; c++) {
      if (arr[r][c] === "c") {
        idx = c;
        res[r][c] = 0;
      } else {
        if (idx !== -1) res[r][c] = c - idx;
      }
    }
  }
  console.log(res.map((x) => x.join(" ")).join("\n"));
}

solution(H, W, arr);
