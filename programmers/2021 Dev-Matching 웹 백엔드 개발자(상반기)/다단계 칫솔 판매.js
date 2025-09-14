function solution(enroll, referral, seller, amount) {
    const n = enroll.length;
    const graph = Array(n).fill(0);
    const answer = Array(n).fill(0);
    referral.forEach((ref, idx) => {
        let parent = enroll.findIndex((x) => x === ref);
        graph[idx] = parent;
    });
    seller.forEach((sel, idx) => {
        let cur = enroll.findIndex((x) => x === sel);
        let income = amount[idx] * 100;
        while (income && cur + 1) {
            const repay = (income / 10) >> 0;
            answer[cur] += income - repay;
            cur = graph[cur];
            income = repay;
        }
    });
    return answer;
}