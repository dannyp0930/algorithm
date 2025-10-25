const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const W = input[1].split(" ").map(Number);

function solution(N, W) {
  let answer = 0;
  const dfs = (arr, res) => {
    if (arr.length === 2) {
      answer = answer > res ? answer : res;
      return;
    }
    for (let i = 1; i < arr.length - 1; i++) {
      dfs(
        [...arr.slice(0, i), ...arr.slice(i + 1)],
        res + arr[i - 1] * arr[i + 1]
      );
    }
  };
  dfs([...W], 0);
  console.log(answer);
}

solution(N, W);
