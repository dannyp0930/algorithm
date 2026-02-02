const fs = require("fs");
const S = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim();

function solution(S) {
  const reg = /^(pi|ka|chu)+$/;
  console.log(reg.test(S) ? "YES" : "NO");
}

solution(S);
