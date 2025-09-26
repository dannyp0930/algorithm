function solution(play_time, adv_time, logs) {
    const getSeconds = (str) => {
        const [h, m, s] = str.split(":").map(Number);
        return h * 3600 + m * 60 + s;
    }
    const getTime = (num) => {
        const h = (num / 3600 >> 0).toString();
        const m = ((num / 60 >> 0) % 60).toString();
        const s = (num % 60).toString();
        return `${h.padStart(2, '0')}:${m.padStart(2, '0')}:${s.padStart(2, '0')}`;
    }
    const [play, adv] = [play_time, adv_time].map(getSeconds);
    if (play === adv) return "00:00:00";
    const timeLine = Array(play).fill(0);
    for (const log of logs) {
        const [ s, e ] = log.split("-").map(getSeconds);
        timeLine[s]++;
        timeLine[e]--;
    }
    for (let i = 0; i < play - 1; i++) timeLine[i + 1] += timeLine[i];
    for (let i = 0; i < play - 1; i++) timeLine[i + 1] += timeLine[i];
    let max = timeLine[adv - 1], idx = 0;
    for (let i = 0; i < play - adv; i++) {
        if (max < timeLine[i + adv] - timeLine[i]) {
            max = timeLine[i + adv] - timeLine[i];
            idx = i + 1;
        }
    }
    return getTime(idx);
}