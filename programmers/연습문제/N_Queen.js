function solution(n) {
    let answer = 0;
    let col = [];
    const promising = (i) => {
        for (let k = 0; k < i; k++) {
            if (col[i] === col[k] || (i - k) === Math.abs(col[i] - col[k])) {
                return false;
            }
        }
        return true;
    }
    const nQueens = (i) => {
        if (i === n) {
            answer++;
            return;
        }
        for (let j = 0; j < n; j++) {
            col[i] = j;
            if (promising(i)) {
                nQueens(i + 1);
            }
        }
    }
    nQueens(0);
    return answer;
}