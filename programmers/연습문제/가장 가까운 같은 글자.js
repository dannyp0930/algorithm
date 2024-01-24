function solution(s) {
  const ans = [...s].map((a, i) => {
    const tmp = s.slice(0, i).lastIndexOf(a);
    return tmp < 0 ? -1 : i - tmp;
  });
  return ans;
}
