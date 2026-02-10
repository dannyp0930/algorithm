const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const a = input.slice(1);

function solution(N, a) {
  const getHeart = () => {
    for (let r = 0; r < N; r++) {
      for (let c = 0; c < N; c++) {
        if (a[r][c] === "*") return [r + 1, c];
      }
    }
  };
  const getHip = (hr, hc) => {
    for (let r = hr + 1; r < N; r++) {
      if (a[r][hc] === "_") return [r - 1, hc];
    }
  };
  const getArms = (hr, hc) => {
    let [left, right] = [0, 0];
    for (let c = hc - 1; c >= 0; c--) {
      if (a[hr][c] === "*") left++;
      else break;
    }
    for (let c = hc + 1; c < N; c++) {
      if (a[hr][c] === "*") right++;
      else break;
    }
    return [left, right];
  };
  const getLegs = (hr, hc) => {
    let [left, right] = [0, 0];
    for (let r = hr + 1; r < N; r++) {
      if (a[r][hc - 1] === "*") left++;
      else break;
    }
    for (let r = hr + 1; r < N; r++) {
      if (a[r][hc + 1] === "*") right++;
      else break;
    }
    return [left, right];
  };
  const heart = getHeart();
  const hip = getHip(...heart);
  const arms = getArms(...heart);
  const legs = getLegs(...hip);

  console.log(heart[0] + 1, heart[1] + 1);
  console.log(...arms, hip[0] - heart[0], ...legs);
}

solution(N, a);
