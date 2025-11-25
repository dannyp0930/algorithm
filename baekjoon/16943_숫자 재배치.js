const fs = require("fs");
const [A, B] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ")
    : fs.readFileSync("input.txt").toString().trim().split(" ");

function solution(A, B) {
  const N = A.length;
  if (N > B.length) return console.log(-1);
  B = Number(B);
  const visited = Array(N).fill(false);
  let answer = -1;
  const perm = (str) => {
    if (str.length === N) {
      const num = Number(str);
      if (num < B && answer < num) answer = num;
    }
    for (let i = 0; i < N; i++) {
      if (!str.length && A[i] === "0") continue;
      if (!visited[i]) {
        visited[i] = true;
        perm(str + A[i]);
        visited[i] = false;
      }
    }
  };
  perm("");
  return console.log(answer);
}

solution(A, B);
