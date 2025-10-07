const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const S = input[0];
  const T = input[1];
  const n = S.length;
  let answer = 0;
  const recur = (string) => {
    if (string.length === n) {
      if (string === S) answer = 1;
      return;
    }
    if (string[string.length - 1] === "A") recur(string.slice(0, string.length - 1));
    if (string[0] === "B") recur(string.slice(1).split("").reverse().join(""));
  };
  recur(T);
  console.log(answer);
}

solution();
