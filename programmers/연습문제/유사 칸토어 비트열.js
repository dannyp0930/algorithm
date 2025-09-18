function solution(n, l, r) {
    let answer = 0;
    for (let i = l - 1; i < r; i++) {
        let q = i / 5 >> 0;
        let r = i % 5;
        while (q) {
            if (r === 2) break;
            r = q % 5;
            q = q / 5 >> 0;
        }
        if (r !== 2) answer++;
    }
    return answer;
}