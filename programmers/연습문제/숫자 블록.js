function solution(begin, end) {
    const answer = [];
    const getDivisor = (num) => {
        if (num === 1) return 0;
        const res = new Set();
        for (let i = 2; i <= num ** (1 / 2); i++) {
            if (!(num % i)) {
                res.add(i);
                if (num / i <= 1e7) {
                    return num / i;
                }
            }
        }
        return res.size ? Math.max(...res) : 1;
    }
    for (let i = begin; i <= end; i++) {
        answer.push(getDivisor(i));
    }
    return answer;
}