const fs = require("fs");
const S =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim();

function solution(S) {
  let idx = 0;
  let n = 1;
  while (true) {
    const nString = n.toString();
    for (const ch of nString) {
      if (S[idx] === ch) {
        idx++;
        if (idx === S.length) {
          console.log(n);
          return;
        }
      }
    }
    n++;
  }
}

solution(S);
