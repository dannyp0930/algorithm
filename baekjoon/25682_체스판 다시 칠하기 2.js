const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M, K] = input[0].split(" ").map(Number);
const board = input.slice(1);

function solution(N, M, K, board) {
  const prefix = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));
  for (let r = 1; r <= N; r++) {
    let rowSum = 0;
    for (let c = 1; c <= M; c++) {
      const expected = (r + c) % 2 ? "B" : "W";
      rowSum += board[r - 1][c - 1] === expected ? 0 : 1;
      prefix[r][c] = prefix[r - 1][c] + rowSum;
    }
  }
  let answer = K * K + 1;
  for (let r = 1; r <= N - K + 1; r++) {
    for (let c = 1; c <= M - K + 1; c++) {
      const [r2, c2] = [r + K - 1, c + K - 1];
      const whiteWrong =
        prefix[r2][c2] -
        prefix[r - 1][c2] -
        prefix[r2][c - 1] +
        prefix[r - 1][c - 1];
      const blackWrong = K * K - whiteWrong;
      answer = Math.min(answer, whiteWrong, blackWrong);
    }
  }
  console.log(answer);
}

solution(N, M, K, board);
