const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input.shift());
const S = input.map((x) => x.split(" ").map(Number));

// 백트래킹
function solution1(N, S) {
  const visited = Array(N).fill(false);
  let answer = 100 * N;
  const getStat = (arr) => {
    let res = 0;
    for (let i = 0; i < arr.length; i++) {
      for (let j = i + 1; j < arr.length; j++) {
        res += S[arr[i]][arr[j]] + S[arr[j]][arr[i]];
      }
    }
    return res;
  };
  const dfs = (start, idx, cnt, k) => {
    if (cnt === k) {
      const link = [];
      for (let i = 0; i < N; i++) {
        if (!visited[i]) link.push(i);
      }
      const startStat = getStat(start);
      const linkStat = getStat(link);
      const diff = Math.abs(startStat - linkStat);
      answer = answer > diff ? diff : answer;
    }
    for (let i = idx; i < N; i++) {
      visited[i] = true;
      start.push(i);
      dfs(start, i + 1, cnt + 1, k);
      visited[i] = false;
      start.pop();
      if (answer === 0) return;
    }
  };
  for (let k = 2; k <= N >> 1; k++) {
    dfs([], 0, 0, k);
    if (answer === 0) break;
  }
  console.log(answer);
}

// 비트마스킹
function solution2(N, S) {
  let answer = 100 * N;
  const getStat = (arr) => {
    let res = 0;
    for (let i = 0; i < arr.length; i++) {
      for (let j = i + 1; j < arr.length; j++) {
        res += S[arr[i]][arr[j]] + S[arr[j]][arr[i]];
      }
    }
    return res;
  };
  for (let mask = 2; mask < (1 << N) - 1; mask++) {
    if ((mask & 1) === 0) continue;
    const start = [];
    const link = [];
    for (let i = 0; i < N; i++) {
      if (mask & (1 << i)) start.push(i);
      else link.push(i);
    }
    const diff = Math.abs(getStat(start) - getStat(link));
    if (diff < answer) answer = diff;
    if (answer === 0) break;
  }
  console.log(answer);
}

solution1(N, S);
solution2(N, S);
