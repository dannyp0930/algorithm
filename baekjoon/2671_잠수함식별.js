const fs = require("fs");
const str =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim();

function solution(str) {
  const regex = /^(100+1+|01)+$/;
  console.log(regex.test(str) ? "SUBMARINE" : "NOISE");
}

solution(str);
