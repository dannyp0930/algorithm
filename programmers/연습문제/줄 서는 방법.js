function solution(n, k) {
    const factorial = (n) => {
        if (n === 1) return 1;
        return n * factorial(n - 1);
    }
    const answer = [];
    const arr = Array.from({ length: n }, (_, i) => i + 1);
    let cnt = k - 1;
    while (arr.length) {
        if (cnt === 0) {
            answer.push(...arr);
            break;
        }
        const fact = factorial(arr.length - 1);
        const idx = (cnt / fact) >> 0;
        cnt %= fact;
        answer.push(arr[idx]);
        arr.splice(idx, 1);
    }
    return answer;
}