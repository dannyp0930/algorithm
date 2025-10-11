const fs = require("fs");
const S =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim();

function solution() {
  const N = S.length;
  const isPalindrome = (string) => {
    let s = 0,
      e = string.length - 1;
    while (s < e) {
      if (string[s] !== string[e]) return false;
      s++;
      e--;
    }
    return true;
  };
  if (isPalindrome(S)) return N;
  for (let i = 0; i < N; i++) {
    if (isPalindrome(S.slice(i))) {
      return N + i;
    }
  }
  return 2 * N - 1;
}

console.log(solution());
