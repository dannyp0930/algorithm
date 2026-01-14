const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const [_, type] = input[0].split(" ");
const names = input.slice(1);

function solution(type, names) {
  const typeToNum = {
    Y: 1,
    F: 2,
    O: 3,
  };
  const nameSet = new Set(names);
  console.log((nameSet.size / typeToNum[type]) >> 0);
}

solution(type, names);
