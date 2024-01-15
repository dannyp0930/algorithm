function solution(n, m, section) {
  let ans = 0, now = 0;
  section.forEach((s) => {
    if (s > now) {
      ans++;
      now = s + m - 1;
    }
  });
  return ans;
}
