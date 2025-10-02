const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const K = Number(input[0]);
  const order = input[1].split(" ").map(Number);
  const tree = Array.from(Array(K), () => []);
  const restore = (arr, level) => {
    if (!arr.length) return;
    const mid = arr.length >> 1;
    tree[level].push(arr[mid]);
    restore(arr.slice(0, mid), level + 1);
    restore(arr.slice(mid + 1), level + 1);
  };
  restore(order, 0);
  console.log(tree.map((a) => a.join(" ")).join("\n"));
}

solution();
