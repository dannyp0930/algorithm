function solution(a) {
    const map = new Map();
    a.forEach((num) => {
        if (map.has(num)) {
            map.set(num, map.get(num) + 1);     
        } else {
            map.set(num, 1);     
        }
    });
    const arr = Array.from(map).sort((a, b) => b[1] - a[1]);
    let answer = 0;
    for (const [k, v] of arr) {
        if (answer >= v * 2) continue;
        let cnt = 0;
        for (let i = 0; i < a.length - 1; i++) {
            if (a[i] === a[i + 1]) continue;
            if (a[i] !== k && a[i + 1] !== k) continue;
            cnt++;
            i++;
        }
        answer = answer > cnt * 2 ? answer : cnt * 2;
    }
    return answer;
}