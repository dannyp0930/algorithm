function solution(want, number, discount) {
  function check(origin, candidate) {
    for (const item in origin) {
      if (origin[item] !== candidate[item]) return false;
    }
    return true;
  }
  let answer = 0;
  dic = {};
  for (let i = 0; i < want.length; i++) {
    dic[want[i]] = number[i];
  }
  for (let i = 0; i <= discount.length - 10; i++) {
    tmp = {};
    for (const item of discount.slice(i, i + 10)) {
      if (item in tmp) {
        tmp[item]++;
      } else {
        tmp[item] = 1;
      }
    }
    if (check(dic, tmp)) {
      answer++;
    }
  }
  return answer;
}
