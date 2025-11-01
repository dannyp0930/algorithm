const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

input.shift();
const arr = input.map(Number);

function solution(arr) {
  const getResult = (res, operator, i) => {
    if (i === operator.length) {
      const expression = getExpression(operator);
      if (expression) res.push(expression);
      return;
    }
    for (let j = 0; j < 3; j++) {
      operator[i] = j;
      getResult(res, operator, i + 1);
    }
  };
  const getExpression = (operator) => {
    let expression = "1";
    for (let i = 0; i < operator.length; i++) {
      const op = operator[i] === 0 ? " " : operator[i] === 1 ? "+" : "-";
      expression += `${op}${i + 2}`;
    }
    const result = expression
      .replaceAll(" ", "")
      .replaceAll("-", "+-")
      .split("+")
      .map(Number)
      .reduce((a, c) => a + c);
    if (!result) return expression;
    return null;
  };
  for (const N of arr) {
    const operator = Array(N - 1).fill(-1);
    const res = [];
    getResult(res, operator, 0);
    console.log(res.join("\n"));
    console.log();
  }
}

solution(arr);
