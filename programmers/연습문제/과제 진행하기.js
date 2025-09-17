function solution(plans) {
    const answer = [];
    const queue = plans.map(([subject, start, time]) => {
        const [h, m] = start.split(":").map(Number);
        return [subject, h * 60 + m, Number(time)];
    }).sort((a, b) => a[1] - b[1]);
    const first = queue.shift();
    const stack = [first];
    let cur = first[1];
    while (queue.length) {
        const next = queue.shift();
        let diff = next[1] - cur;
        cur = next[1];
        while (stack.length && diff) {
            const now = stack.pop();
            if (now[2] <= diff) {
                answer.push(now[0]);
                diff -= now[2];
            } else {
                now[2] -= diff;
                diff = 0;
                stack.push(now);
            }
        }
        stack.push(next);
    }
    while (stack.length) {
        answer.push(stack.pop()[0]);
    }
    return answer;
}