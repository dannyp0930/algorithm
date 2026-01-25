const fs = require("fs");
const str = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim();

function solution(str) {
  const isCpp = /_/.test(str);
  const isJava = /[A-Z]/.test(str);
  if (isCpp && isJava) return "Error!";
  if (isCpp) {
    if (str.startsWith("_")) return "Error!";
    if (str.endsWith("_")) return "Error!";
    if (/__/.test(str)) return "Error!";
    return str.replace(/_([a-z])/g, (_, char) => char.toUpperCase());
  } else {
    if (/^[A-Z]/.test(str)) return "Error!";
    return str.replace(/[A-Z]/g, (match) => `_${match.toLowerCase()}`);
  }
}

console.log(solution(str));
