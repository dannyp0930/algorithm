const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const options = input.slice(1);

function findShortcut(opt, shortcut) {
  const words = opt.split(" ");
  let idx = 0;
  for (const word of words) {
    const upper = word[0].toUpperCase();
    if (!shortcut.has(upper)) {
      shortcut.add(upper);
      return idx;
    }
    idx += word.length + 1;
  }
  for (let i = 0; i < opt.length; i++) {
    if (opt[i] === " ") continue;
    const upper = opt[i].toUpperCase();
    if (!shortcut.has(upper)) {
      shortcut.add(upper);
      return i;
    }
  }
  return -1;
}

function solution(options) {
  const shortcut = new Set();
  const result = [];
  for (const opt of options) {
    const k = findShortcut(opt, shortcut);
    result.push(
      k === -1 ? opt : `${opt.slice(0, k)}[${opt[k]}]${opt.slice(k + 1)}`
    );
  }
  console.log(result.join("\n"));
}

solution(options);
