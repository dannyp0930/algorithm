function solution(A, B) {
  let answer = 0;
  const ascend = (a, b) => a - b;
  A.sort(ascend);
  B.sort(ascend);
  let j = 0;
  for (let i = 0; i < A.length; i++) {
    if (A[j] < B[i]) {
      answer++;
      j++;
    }
  }
  return answer;
}
