function solution(k, tangerine) {
  let ans = 0;
  const type = {};
  tangerine.forEach((item) => {
    if (type[item]) {
      type[item]++;
    } else {
      type[item] = 1;
    }
  });
  const cnt = Object.values(type).sort((a, b) => b - a);
  for (let num of cnt) {
    ans++;
    if (k > num) k -= num;
    else break;
  }
  return ans;
}
