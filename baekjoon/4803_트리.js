const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const isTree = (i, p, graph, visit) => {
    visit[i] = true;
    for (const v of graph[i]) {
      if (!visit[v]) {
        if (!isTree(v, i, graph, visit)) return false;
      } else if (v !== p) return false;
    }
    return true;
  };
  const pringResult = (t, cnt) => {
    let sentence = "";
    if (!cnt) {
      sentence = "No trees.";
    } else if (cnt === 1) {
      sentence = "There is one tree.";
    } else {
      sentence = `A forest of ${cnt} trees.`;
    }
    console.log(`Case ${t}: ${sentence}`);
  };
  let i = 0;
  let t = 1;
  while (true) {
    const [n, m] = input[i].split(" ").map(Number);
    if (!n && !m) break;
    const edges = input
      .slice(i + 1, i + m + 1)
      .map((x) => x.split(" ").map(Number));
    const graph = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of edges) {
      graph[a].push(b);
      graph[b].push(a);
    }
    const visit = Array(n + 1).fill(false);
    let cnt = 0;
    for (let i = 1; i <= n; i++) {
      if (!visit[i] && isTree(i, i, graph, visit)) cnt++;
    }
    pringResult(t, cnt);
    i += m + 1;
    t++;
  }
}

solution();
