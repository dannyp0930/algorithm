const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map(Number);
const O = input[2].split(" ").map(Number);

function solution(N, A, O) {
  let maxNum = -1000000000;
  let minNum = 1000000000;
  const calc = (string) => {
    let res = A[0];
    for (let i = 0; i < N - 1; i++) {
      if (string[i] === "0") {
        res += A[i + 1];
      } else if (string[i] === "1") {
        res -= A[i + 1];
      } else if (string[i] === "2") {
        res *= A[i + 1];
      } else {
        if (res < 0) {
          res = -((-res / A[i + 1]) >> 0);
        } else {
          res = (res / A[i + 1]) >> 0;
        }
      }
    }
    maxNum = maxNum > res ? maxNum : res;
    minNum = minNum < res ? minNum : res;
  };
  const dfs = (string, arr) => {
    if (string.length === N - 1) {
      calc(string);
      return;
    }
    for (let i = 0; i < 4; i++) {
      const newArr = [...arr];
      if (newArr[i]) {
        newArr[i]--;
        dfs(string + i, newArr);
      }
    }
  };
  dfs("", [...O]);
  console.log(`${maxNum}\n${minNum}`);
}

solution(N, A, O);
