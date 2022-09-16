function solution(n, s) {
  share = parseInt(s / n);
  if (share === 0) {
      return [-1];
  }
  rest = s % n;
  let ans = new Array(n).fill(share)
  for (let i = 0; i < rest; i++) {
      ans[n - i - 1]++;
  }
  return ans;
}