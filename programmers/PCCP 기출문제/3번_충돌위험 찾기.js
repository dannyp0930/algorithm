function solution(points, routes) {
    let answer = 0;
    const move = (s, e) => {
        const res = [];
        let [r, c] = s;
        const [er, ec] = e;
        while (r !== er || c !== ec) {
            res.push([r, c]);
            if (r !== er) {
                if (r < er) {
                    r++;
                } else {
                    r--;
                }
            } else {
                if (c < ec) {
                    c++;
                } else {
                    c--;
                }
            }
        }
        return res;
    }
    let maxLength = 0;
    const schedule = routes.map((route) => {
        const res = [];
        for (let i = 0; i < route.length - 1; i++) {
            const [start, end] = [points[route[i] - 1], points[route[i + 1] - 1]];
            res.push(...move(start, end));
            if (i === route.length - 2) {
                res.push(end);
            }
        }
        maxLength = maxLength < res.length ? res.length : maxLength;
        return res;
    });
    const n = routes.length;
    for (let i = 0; i < maxLength; i++) {
        const position = new Map();
        let arrive = 0;
        for (let j = 0; j < n; j++) {
            if (schedule[j][i]) {
                const pos = schedule[j][i].join(',')
                if (position[pos]) {
                    position[pos]++;
                } else {
                    position[pos] = 1;
                }
            }
        }
        Object.values(position).forEach((value) => {
            if (value > 1) {
                answer++;
            }
        });
    }
    return answer;
}