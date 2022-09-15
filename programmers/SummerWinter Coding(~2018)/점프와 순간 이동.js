function solution(n) {
  var ans = 0;
  while (n) {
      if (n % 2) {
          n = (n - 1) / 2;
          ans++;
      } else {
          n /= 2;
      }
  }
  return ans;
}