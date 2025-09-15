function solution(a) {
    let answer = 1;
    const n = a.length;
    let min = Infinity, minIdx = 0;
    a.forEach((v, i) => {
        if (min > v) {
            min = v;
            minIdx = i;
        }
    });
    let tmp = Infinity;
    for (let i = 0; i < minIdx; i++) {
        if (tmp > a[i]) {
            tmp = a[i];
            answer++;
        }
    }
    tmp = Infinity;
    for (let i = n - 1; i > minIdx; i--) {
        if (tmp > a[i]) {
            tmp = a[i];
            answer++;
        }
    }
    return answer;
}