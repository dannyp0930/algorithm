const fs = require("fs");
const [A, B] =
  process.platform === "linux"
    ? fs
        .readFileSync(0, "utf-8")
        .toString()
        .trim()
        .split("\n")
        .map((x) => x.trim())
    : fs
        .readFileSync("input.txt")
        .toString()
        .trim()
        .split("\n")
        .map((x) => x.trim());

function solution(A, B) {
  const romanToDecimal = (S) => {
    const value = {
      I: 1,
      V: 5,
      X: 10,
      L: 50,
      C: 100,
      D: 500,
      M: 1000,
    };
    let res = 0;
    for (let i = 0; i < S.length; i++) {
      const cur = value[S[i]];
      const next = value[S[i + 1]];
      if (next && cur < next) res -= cur;
      else res += cur;
    }
    return res;
  };
  const decimalToRoman = (N) => {
    const val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const sym = [
      "M",
      "CM",
      "D",
      "CD",
      "C",
      "XC",
      "L",
      "XL",
      "X",
      "IX",
      "V",
      "IV",
      "I",
    ];
    let res = "";
    for (let i = 0; i < val.length; i++) {
      while (N >= val[i]) {
        N -= val[i];
        res += sym[i];
      }
    }
    return res;
  };
  const a = romanToDecimal(A);
  const b = romanToDecimal(B);
  console.log(a + b);
  console.log(decimalToRoman(a + b));
}

solution(A, B);
