const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split("\n").map(Number);

function solution(input) {
  const memo = new Map();
  const recur = (len) => {
    if (len === 1) return "-";
    if (memo.has(len)) return memo.get(len);
    const part = recur(len / 3);
    const str = part + " ".repeat(len / 3) + part;
    memo.set(len, str);
    return str;
  };
  const res = [];
  for (const N of input) {
    res.push(recur(3 ** N));
  }
  console.log(res.join("\n"));
}

solution(input);
