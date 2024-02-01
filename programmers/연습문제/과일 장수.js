function solution(k, m, score) {
  let ans = 0;
  const n = score.length;
  score.sort((a, b) => b - a);
  for (let i = 0; i < n - m + 1; i += m) {
    ans += score[i + m - 1] * m;
  }
  return ans;
}
