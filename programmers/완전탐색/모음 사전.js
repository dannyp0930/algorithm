function solution(word) {
  let ans = 0;
  const dic = { A: 0, E: 1, I: 2, O: 3, U: 4 };
  const num = [781, 156, 31, 6, 1];
  const array = [...word];
  array.forEach((ch, i) => {
    ans += dic[ch] * num[i] + 1;
  });
  return ans;
}