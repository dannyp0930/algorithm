const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M, R] = input[0].split(" ").map(Number);
const A = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(N, M, R, A) {
  const L = (N > M ? M : N) >> 1;
  for (let l = 0; l < L; l++) {
    const [top, left, bottom, right] = [l, l, N - l - 1, M - l - 1];
    const tmp = [];
    for (let c = left; c <= right; c++) tmp.push(A[top][c]);
    for (let r = top + 1; r <= bottom; r++) tmp.push(A[r][right]);
    for (let c = right - 1; c >= left; c--) tmp.push(A[bottom][c]);
    for (let r = bottom - 1; r > top; r--) tmp.push(A[r][left]);
    const len = tmp.length;
    const rot = R % len;
    const rotated = tmp.slice(rot).concat(tmp.slice(0, rot));
    let idx = 0;
    for (let c = left; c <= right; c++) A[top][c] = rotated[idx++];
    for (let r = top + 1; r <= bottom; r++) A[r][right] = rotated[idx++];
    for (let c = right - 1; c >= left; c--) A[bottom][c] = rotated[idx++];
    for (let r = bottom - 1; r > top; r--) A[r][left] = rotated[idx++];
  }
  console.log(A.map((x) => x.join(" ")).join("\n"));
}

solution(N, M, R, A);
