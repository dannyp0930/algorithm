const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [K, L] = input[0].split(" ").map(Number);
const ID = input.slice(1);

function solution(K, L, ID) {
  const queue = new Map();
  for (let i = 0; i < L; i++) {
    const id = ID[i];
    if (queue.has(id)) {
      queue.delete(id);
    }
    queue.set(id, true);
  }
  console.log(Array.from(queue.keys()).slice(0, K).join("\n"));
}

solution(K, L, ID);
