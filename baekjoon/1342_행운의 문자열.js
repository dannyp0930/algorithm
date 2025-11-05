const fs = require("fs");
const S =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim();

function solution(S) {
  const dic = new Map();
  const N = S.length;
  for (const ch of S) {
    if (dic.has(ch)) {
      dic.set(ch, dic.get(ch) + 1);
    } else {
      dic.set(ch, 1);
    }
  }
  let answer = 0;
  const dfs = (cnt, cur) => {
    if (cnt === N) {
      answer++;
      return;
    }
    for (const [c, n] of dic) {
      if (n && cur !== c) {
        dic.set(c, n - 1);
        dfs(cnt + 1, c);
        dic.set(c, n);
      }
    }
  };
  dfs(0, "");
  console.log(answer);
}

solution(S);
