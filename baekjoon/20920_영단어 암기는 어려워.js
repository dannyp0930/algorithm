const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const words = input.slice(1);

function solution(N, M, words) {
  const book = new Map();
  for (let i = 0; i < N; i++) {
    const word = words[i];
    if (word.length >= M) {
      const cnt = book.get(word);
      if (cnt) book.set(word, cnt + 1);
      else book.set(word, 1);
    }
  }
  const res = Array.from(book)
    .sort((a, b) =>
      a[1] === b[1]
        ? a[0].length === b[0].length
          ? a[0].localeCompare(b[0])
          : b[0].length - a[0].length
        : b[1] - a[1]
    )
    .map((x) => x[0]);
  console.log(res.join("\n"));
}

solution(N, M, words);
