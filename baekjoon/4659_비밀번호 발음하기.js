const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(input) {
  const res = [];
  const vowels = ["a", "e", "i", "o", "u"];
  const acceptable = (str) => {
    const N = str.length;
    let hasVowel = false;
    let vowelCnt = 0;
    let consCnt = 0;
    for (let i = 0; i < N; i++) {
      const c = str[i];
      if (vowels.includes(c)) {
        hasVowel = true;
        vowelCnt++;
        consCnt = 0;
      } else {
        consCnt++;
        vowelCnt = 0;
      }
      if (vowelCnt === 3 || consCnt === 3) return false;
      if (i > 0 && c !== "e" && c !== "o" && c === str[i - 1]) {
        return false;
      }
    }
    return hasVowel;
  };
  for (const str of input) {
    if (str === "end") break;
    res.push(`<${str}> is ${acceptable(str) ? "" : "not "}acceptable.`);
  }
  console.log(res.join("\n"));
}

solution(input);
