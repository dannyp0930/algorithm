const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input.shift(0).split(" ").map(Number);
const C = input.pop().split(" ").map(Number);
const A = input.map((x) => x.split(" ").map(Number));

function solution(N, M, A, C) {
  const calc1 = () => {
    for (let r = 0; r < N >> 1; r++) {
      [A[r], A[N - r - 1]] = [A[N - r - 1], A[r]];
    }
  };
  const calc2 = () => {
    for (let r = 0; r < N; r++) {
      for (let c = 0; c < M >> 1; c++) {
        [A[r][c], A[r][M - c - 1]] = [A[r][M - c - 1], A[r][c]];
      }
    }
  };
  const calc3 = () => {
    const rotated = Array.from({ length: M }, () => Array(N).fill(0));
    for (let r = 0; r < N; r++) {
      for (let c = 0; c < M; c++) {
        rotated[c][N - 1 - r] = A[r][c];
      }
    }
    A = rotated;
    [N, M] = [M, N];
  };
  const calc4 = () => {
    const rotated = Array.from({ length: M }, () => Array(N).fill(0));
    for (let r = 0; r < N; r++) {
      for (let c = 0; c < M; c++) {
        rotated[M - 1 - c][r] = A[r][c];
      }
    }
    A = rotated;
    [N, M] = [M, N];
  };
  const calc5 = () => {
    const Q1 = Array.from({ length: N >> 1 }, () => Array(M >> 1).fill(0));
    const Q2 = Array.from({ length: N >> 1 }, () => Array(M >> 1).fill(0));
    const Q3 = Array.from({ length: N >> 1 }, () => Array(M >> 1).fill(0));
    const Q4 = Array.from({ length: N >> 1 }, () => Array(M >> 1).fill(0));
    for (let r = 0; r < N >> 1; r++) {
      for (let c = 0; c < M >> 1; c++) {
        Q1[r][c] = A[r][c];
        Q2[r][c] = A[r][c + (M >> 1)];
        Q3[r][c] = A[r + (N >> 1)][c + (M >> 1)];
        Q4[r][c] = A[r + (N >> 1)][c];
      }
    }
    for (let r = 0; r < N >> 1; r++) {
      for (let c = 0; c < M >> 1; c++) {
        A[r][c + (M >> 1)] = Q1[r][c];
        A[r + (N >> 1)][c + (M >> 1)] = Q2[r][c];
        A[r + (N >> 1)][c] = Q3[r][c];
        A[r][c] = Q4[r][c];
      }
    }
  };
  const calc6 = () => {
    const Q1 = Array.from({ length: N >> 1 }, () => Array(M >> 1).fill(0));
    const Q2 = Array.from({ length: N >> 1 }, () => Array(M >> 1).fill(0));
    const Q3 = Array.from({ length: N >> 1 }, () => Array(M >> 1).fill(0));
    const Q4 = Array.from({ length: N >> 1 }, () => Array(M >> 1).fill(0));
    for (let r = 0; r < N >> 1; r++) {
      for (let c = 0; c < M >> 1; c++) {
        Q1[r][c] = A[r][c];
        Q2[r][c] = A[r][c + (M >> 1)];
        Q3[r][c] = A[r + (N >> 1)][c + (M >> 1)];
        Q4[r][c] = A[r + (N >> 1)][c];
      }
    }
    for (let r = 0; r < N >> 1; r++) {
      for (let c = 0; c < M >> 1; c++) {
        A[r + (N >> 1)][c] = Q1[r][c];
        A[r][c] = Q2[r][c];
        A[r][c + (M >> 1)] = Q3[r][c];
        A[r + (N >> 1)][c + (M >> 1)] = Q4[r][c];
      }
    }
  };
  for (const c of C) {
    switch (c) {
      case 1:
        calc1();
        break;
      case 2:
        calc2();
        break;
      case 3:
        calc3();
        break;
      case 4:
        calc4();
        break;
      case 5:
        calc5();
        break;
      case 6:
        calc6();
        break;
    }
  }
  for (const arr of A) {
    console.log(arr.join(" "));
  }
}

solution(N, M, A, C);
