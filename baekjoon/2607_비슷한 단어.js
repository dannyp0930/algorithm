const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const N = Number(input.shift());
  const wordToNumCnt = (word) => {
    const arr = Array(26).fill(0);
    for (const chr of word) {
      arr[chr.charCodeAt(0) - 65]++;
    }
    return arr;
  };
  const isSimilar = (a, b) => {
    let diffA = 0,
      diffB = 0;
    for (let i = 0; i < 26; i++) {
      if (a[i] > b[i]) diffA += a[i] - b[i];
      else if (a[i] < b[i]) diffB += b[i] - a[i];
    }
    return (
      (!diffA && !diffB) ||
      (diffA === 1 && diffB === 1) ||
      (diffA === 1 && !diffB) ||
      (!diffA && diffB === 1)
    );
  };
  const word = input.shift();
  const base = wordToNumCnt(word);
  let answer = 0;
  for (let i = 0; i < N - 1; i++) {
    const compare = wordToNumCnt(input[i]);
    if (isSimilar(base, compare)) answer++;
  }
  console.log(answer);
}

solution();
