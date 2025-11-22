const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const [mp, mf, ms, mv] = input[1].split(" ").map(Number);
const ings = input.slice(2).map((x) => x.split(" ").map(Number));

function solution(N, mp, mf, ms, mv, ings) {
  const satisfy = (p, f, s, v) => p >= mp && f >= mf && s >= ms && v >= mv;
  let answer = 75000;
  let result;
  const select = [];
  const updateResult = () => {
    for (let i = 0; i < Math.min(result.length, select.length); i++) {
      if (select[i] < result[i]) {
        result = [...select];
        return;
      } else if (select[i] > result[i]) return;
    }
    if (select.length < result.length) result = [...select];
  };
  const checkResult = (cp, cf, cs, cv, cc) => {
    if (satisfy(cp, cf, cs, cv)) {
      if (cc < answer) {
        answer = cc;
        result = [...select];
      } else if (cc === answer) updateResult();
    }
  };
  const dfs = (idx, cp, cf, cs, cv, cc) => {
    if (idx === N) return checkResult(cp, cf, cs, cv, cc);
    const [p, f, s, v, c] = ings[idx];
    select.push(idx + 1);
    dfs(idx + 1, cp + p, cf + f, cs + s, cv + v, cc + c);
    select.pop();
    dfs(idx + 1, cp, cf, cs, cv, cc);
  };
  dfs(0, 0, 0, 0, 0, 0);
  if (answer < 75000) {
    console.log(answer);
    console.log(result.join(" "));
  } else {
    console.log(-1);
  }
}

solution(N, mp, mf, ms, mv, ings);
