function solution(line) {
    const n = line.length;
    const stars = [];
    let minX = Number.MAX_SAFE_INTEGER;
    let minY = Number.MAX_SAFE_INTEGER;
    let maxY = Number.MIN_SAFE_INTEGER;
    let maxX = Number.MIN_SAFE_INTEGER;
    const comb = (arr, idx) => {
        if (arr.length === 2) {
            const [a, b, e] = line[arr[0]];
            const [c, d, f] = line[arr[1]];
            const slope = a * d - b * c
            if (!slope) return;
            let x = (b * f - e * d) / slope;
            let y = (e * c - a * f) / slope;
            if (x % 1 || y % 1) return;
            minX = Math.min(minX, x);
            minY = Math.min(minY, y);
            maxX = Math.max(maxX, x);
            maxY = Math.max(maxY, y);
            stars.push([x, y]);
            return;
        }
        for (let i = idx; i < n; i++) {
            arr.push(i);
            comb([...arr], i + 1);
            arr.pop(i);
        }
    }
    comb([], 0);
    const answer = Array.from(Array(maxY - minY + 1), () => Array(maxX - minX + 1).fill('.'));
    stars.forEach(([x, y]) => {
        answer[maxY - y][x - minX] = '*';
    })
    return answer.map((ans) => ans.join(''));
}