function solution(a, b, n) {
  let ans = 0;
  while (n >= a) {
    const share = parseInt(n / a);
    const reminder = n % a;
    ans += share * b;
    n = share * b + reminder;
  }
  return ans;
}
