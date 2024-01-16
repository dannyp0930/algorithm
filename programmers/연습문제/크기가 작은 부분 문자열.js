function solution(t, p) {
  let ans = 0;
  const num = parseInt(p);
  for (let i = 0; i < t.length - p.length + 1; i++) {
    const tmp = parseInt(t.slice(i, i + p.length));
    if (num >= tmp) {
      ans++;
    }
  }
  return ans;
}
