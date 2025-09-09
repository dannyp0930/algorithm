function solution(r1, r2) {
    let answer = 0;
    for (let i = 1; i <= r2; i++) {
        const maxCnt = Math.floor((r2 ** 2 - i ** 2) ** (1 / 2));
        const minCnt = i >= r1 ? 0 : Math.ceil((r1 ** 2 - i ** 2) ** (1 / 2));
        answer += maxCnt - minCnt + 1;
    }
    return answer * 4;
}