function solution(survey, choices) {
  let answer = '';
  let indc = {
      'R': 0, 'T': 0, 'C': 0, 'F': 0,
      'J': 0, 'M': 0, 'A': 0, 'N': 0
  };
  const result = survey.map((v, i) => {
      if (choices[i] < 4) indc[v[0]] += 4 - choices[i]
      if (choices[i] > 4) indc[v[1]] += choices[i] - 4
  });
  indc['R'] >= indc['T'] ? answer += 'R' : answer += 'T';
  indc['C'] >= indc['F'] ? answer += 'C' : answer += 'F';
  indc['J'] >= indc['M'] ? answer += 'J' : answer += 'M';
  indc['A'] >= indc['N'] ? answer += 'A' : answer += 'N';
  return answer;
}