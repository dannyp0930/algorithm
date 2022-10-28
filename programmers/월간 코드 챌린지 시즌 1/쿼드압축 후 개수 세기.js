function solution(arr) {
  const answer = [0, 0];
  const l = arr.length;
  function quadTree(r, c, l) {
    const n = arr[r][c];
    for (let i = r; i < r + l; i++) {
      for (let j = c; j < c + l; j++) {
        if (arr[i][j] != n) {
          l = parseInt(l / 2);
          quadTree(r, c, l);
          quadTree(r, c + l, l);
          quadTree(r + l, c, l);
          quadTree(r + l, c + l, l);
          return;
        }
      }
    }
    answer[n]++;
  }
  quadTree(0, 0, l);
  return answer;
}
