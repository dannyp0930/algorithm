const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(input) {
  const isValid = (T) => {
    const cntX = T.filter((x) => x === "X").length;
    const cntO = T.filter((x) => x === "O").length;
    if (!(cntX === cntO || cntX === cntO + 1)) return false;
    let winX = false;
    let winO = false;
    const line = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];
    for (const [a, b, c] of line) {
      if (T[a] === T[b] && T[a] === T[c]) {
        if (T[a] === "X") winX = true;
        if (T[a] === "O") winO = true;
      }
    }
    if (winX && winO) return false;
    if (winX && cntX !== cntO + 1) return false;
    if (winO && cntX !== cntO) return false;
    if (!winX && !winO && cntX + cntO !== 9) return false;
    return true;
  };
  for (const test of input) {
    if (test === "end") break;
    console.log(isValid(test.split("")) ? "valid" : "invalid");
  }
}

solution(input);
